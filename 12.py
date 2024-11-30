import unittest
from functools import wraps


def coroutine(gen):
    @wraps(gen)
    def patched():
        itr = gen()
        next(itr)
        return itr

    return patched


@coroutine
def storage():
    values = set()
    was_there = False
    while True:
        val = yield was_there
        was_there = val in values
        if not was_there:
            values.add(val)


class TestStorage(unittest.TestCase):
    def test_basic_usage(self):
        st = storage()
        self.assertFalse(st.send(1))
        self.assertTrue(st.send(1))
        self.assertFalse(st.send(2))
        self.assertTrue(st.send(2))
        self.assertTrue(st.send(1))

    def test_various_types(self):
        st = storage()
        self.assertFalse(st.send("test"))
        self.assertTrue(st.send("test"))
        self.assertFalse(st.send((1, 2)))
        self.assertTrue(st.send((1, 2)))
        self.assertFalse(st.send(None))
        self.assertTrue(st.send(None))

    def test_edge_cases(self):
        st = storage()
        self.assertFalse(st.send(""))
        self.assertTrue(st.send(""))
        self.assertFalse(st.send("@!#"))
        self.assertTrue(st.send("@!#"))

    def test_non_hashable(self):
        st = storage()
        with self.assertRaises(TypeError):
            st.send([1, 2, 3])

    def test_no_initial_send(self):
        st = storage()
        try:
            st.send(1)
        except Exception as e:
            self.fail(f"Initialization failed with exception {e}")

    def test_reset_storage(self):
        st = storage()
        st.send(1)
        st.send(2)
        st = storage()
        self.assertFalse(st.send(1))


if __name__ == '__main__':
    unittest.main()
