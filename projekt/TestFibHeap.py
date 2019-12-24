import unittest
from FibHeap import FibHeap


class TestQueue(unittest.TestCase):

    def test_error_show(self):
        heap_test_show = FibHeap()
        self.assertEqual(heap_test_show.show_main_nodes(), "")
        heap_test_show.push(5)
        heap_test_show.push(2)
        heap_test_show.push(9)
        heap_test_show.push(11)
        self.assertEqual(heap_test_show.show_main_nodes(), "5 2 9 11 ")
        self.assertEqual(heap_test_show.show_all_nodes(), "5 2 9 11 ")

    def test_error_push(self):
        heap = FibHeap()
        self.assertEqual(heap.show_main_nodes(), "")
        heap.push(5)
        self.assertEqual(heap.show_main_nodes(), "5 ")
        heap.push(2)
        self.assertEqual(heap.show_main_nodes(), "5 2 ")
        heap.push(9)
        self.assertEqual(heap.show_main_nodes(), "5 2 9 ")
        heap.push(11)
        self.assertEqual(heap.show_main_nodes(), "5 2 9 11 ")
        self.assertEqual(heap.show_all_nodes(), "5 2 9 11 ")

    def test_error_cutting(self):
        heap_test_pop = FibHeap()
        self.assertEqual(heap_test_pop.show_main_nodes(), "")
        heap_test_pop.push(5)
        self.assertEqual(heap_test_pop.show_main_nodes(), "5 ")
        heap_test_pop.push(2)
        self.assertEqual(heap_test_pop.show_main_nodes(), "5 2 ")
        heap_test_pop.push(9)
        self.assertEqual(heap_test_pop.show_main_nodes(), "5 2 9 ")
        heap_test_pop.push(11)
        self.assertEqual(heap_test_pop.show_main_nodes(), "5 2 9 11 ")
        self.assertEqual(heap_test_pop.pop(), 2)
        self.assertEqual(heap_test_pop.show_main_nodes(), "5 11 ")
        self.assertEqual(heap_test_pop.show_all_nodes(), "5 9 11 ")

    def test_error_cutting2(self):
        heap_test_pop = FibHeap()
        heap_test_pop.push(5)
        heap_test_pop.push(2)
        heap_test_pop.push(9)
        heap_test_pop.push(11)
        heap_test_pop.push(1)
        heap_test_pop.push(4)
        self.assertEqual(heap_test_pop.show_main_nodes(), "5 2 9 11 1 4 ")
        self.assertEqual(heap_test_pop.pop(), 1)
        self.assertEqual(heap_test_pop.show_main_nodes(), "2 4 ")
        self.assertEqual(heap_test_pop.show_all_nodes(), "2 9 11 5 4 ")

    def test_error_cutting3(self):
        heap_test_pop = FibHeap()
        heap_test_pop.push(2)
        heap_test_pop.push(7)
        heap_test_pop.push(9)
        heap_test_pop.push(11)
        self.assertEqual(heap_test_pop.show_main_nodes(), "2 7 9 11 ")
        self.assertEqual(heap_test_pop.pop(), 2)
        self.assertEqual(heap_test_pop.show_main_nodes(), "7 11 ")
        self.assertEqual(heap_test_pop.show_all_nodes(), "7 9 11 ")

    def test_error_cutting4(self):
        heap_test_pop = FibHeap()
        heap_test_pop.push(11)
        heap_test_pop.push(7)
        heap_test_pop.push(9)
        heap_test_pop.push(2)
        self.assertEqual(heap_test_pop.show_main_nodes(), "11 7 9 2 ")
        self.assertEqual(heap_test_pop.pop(), 2)
        self.assertEqual(heap_test_pop.show_main_nodes(), "7 9 ")
        self.assertEqual(heap_test_pop.show_all_nodes(), "7 11 9 ")

    def test_error_cutting5(self):
        heap_test_pop = FibHeap()
        heap_test_pop.push(2)
        self.assertEqual(heap_test_pop.show_main_nodes(), "2 ")
        self.assertEqual(heap_test_pop.pop(), 2)
        self.assertEqual(heap_test_pop.show_main_nodes(), "")
        self.assertEqual(heap_test_pop.show_all_nodes(), "")

    def test_error_is_empty(self):
        heap = FibHeap()
        self.assertEqual(heap.is_empty(), True)
        heap.push(5)
        self.assertEqual(heap.is_empty(), False)

    def test_error_is_decrease(self):
        heap = FibHeap()
        self.assertEqual(heap.is_empty(), True)
        heap.push(5)
        self.assertEqual(heap.is_empty(), False)
        heap.decrease_key(5, 2)
        self.assertEqual(heap.show_all_nodes(), "2 ")
        heap.push(11)
        heap.push(7)
        heap.push(9)
        heap.push(19)
        heap.push(3)
        self.assertEqual(heap.show_all_nodes(), "2 11 7 9 19 3 ")
        self.assertEqual(heap.pop(), 2)
        self.assertEqual(heap.show_all_nodes(), "7 9 19 11 3 ")
        self.assertEqual(heap.show_main_nodes(), "7 3 ")

    def test_error_is_remove(self):
        heap_remove = FibHeap()
        heap_remove.push(4)
        self.assertEqual(heap_remove.is_empty(), False)
        heap_remove.decrease_key(4, 2)
        heap_remove.push(11)
        heap_remove.push(7)
        heap_remove.push(9)
        heap_remove.push(19)
        heap_remove.push(3)
        self.assertEqual(heap_remove.show_all_nodes(), "2 11 7 9 19 3 ")
        self.assertEqual(heap_remove.pop(), 2)
        self.assertEqual(heap_remove.show_all_nodes(), "7 9 19 11 3 ")
        self.assertEqual(heap_remove.show_main_nodes(), "7 3 ")
        heap_remove.remove(7)
        self.assertEqual(heap_remove.show_main_nodes(), "3 9 11 ")
        self.assertEqual(heap_remove.show_all_nodes(), "3 9 19 11 ")
        heap_remove.push(12)
        heap_remove.push(22)
        heap_remove.push(6)
        self.assertEqual(heap_remove.pop(), 3)
        self.assertEqual(heap_remove.show_main_nodes(), "9 6 ")
        self.assertEqual(heap_remove.show_all_nodes(), "9 11 12 19 6 22 ")
        # 9       6
        # 11 19   22
        # 12
        heap_remove.remove(11)
        self.assertEqual(heap_remove.show_all_nodes(), "9 19 6 22 12 ")
        self.assertEqual(heap_remove.show_main_nodes(), "9 6 12 ")
        # 9    6   12
        # 19   22
        heap_remove.push(14)
        heap_remove.push(1)
        heap_remove.push(30)
        heap_remove.push(44)
        heap_remove.push(66)
        heap_remove.push(2)
        self.assertEqual(heap_remove.pop(), 1)
        self.assertEqual(heap_remove.show_all_nodes(), "6 12 30 44 14 9 19 22 2 66 ")
        self.assertEqual(heap_remove.show_main_nodes(), "6 2 ")
        # 6                       2
        # 12       9   22        66
        # 30 14    19
        # 44
        self.assertEqual(heap_remove.pop(), 2)
        self.assertEqual(heap_remove.show_all_nodes(), "6 12 30 44 14 9 19 22 66 ")
        self.assertEqual(heap_remove.show_main_nodes(), "6 66 ")
        self.assertEqual(heap_remove.pop(), 6)
        self.assertEqual(heap_remove.show_all_nodes(), "9 12 30 44 14 22 66 19 ")
        self.assertEqual(heap_remove.show_main_nodes(), "9 ")
        self.assertEqual(heap_remove.pop(), 9)
        self.assertEqual(heap_remove.show_all_nodes(), "12 30 44 14 22 66 19 ")
        self.assertEqual(heap_remove.show_main_nodes(), "12 22 19 ")
        self.assertEqual(heap_remove.pop(), 12)
        self.assertEqual(heap_remove.show_all_nodes(), "22 30 44 66 14 19 ")
        self.assertEqual(heap_remove.show_main_nodes(), "22 14 ")
        self.assertEqual(heap_remove.pop(), 14)
        self.assertEqual(heap_remove.show_all_nodes(), "22 30 44 66 19 ")
        self.assertEqual(heap_remove.show_main_nodes(), "22 19 ")
        self.assertEqual(heap_remove.pop(), 19)
        self.assertEqual(heap_remove.show_all_nodes(), "22 30 44 66 ")
        self.assertEqual(heap_remove.show_main_nodes(), "22 ")
        self.assertEqual(heap_remove.pop(), 22)
        self.assertEqual(heap_remove.show_all_nodes(), "30 44 66 ")
        self.assertEqual(heap_remove.show_main_nodes(), "30 66 ")
        self.assertEqual(heap_remove.pop(), 30)
        self.assertEqual(heap_remove.show_all_nodes(), "44 66 ")
        self.assertEqual(heap_remove.show_main_nodes(), "44 ")
        self.assertEqual(heap_remove.pop(), 44)
        self.assertEqual(heap_remove.show_all_nodes(), "66 ")
        self.assertEqual(heap_remove.show_main_nodes(), "66 ")
        self.assertEqual(heap_remove.pop(), 66)
        self.assertEqual(heap_remove.show_all_nodes(), "")
        self.assertEqual(heap_remove.show_main_nodes(), "")
        self.assertEqual(heap_remove.is_empty(), True)
        self.assertEqual(heap_remove.size(), 0)

        def test_error_is_remove2(self):
            heap_remove = FibHeap()
            heap_remove.push(4)
            self.assertEqual(heap_remove.is_empty(), False)
            heap_remove.decrease_key(4, 2)
            heap_remove.push(11)
            heap_remove.push(7)
            heap_remove.push(9)
            heap_remove.push(19)
            heap_remove.push(3)
            self.assertEqual(heap_remove.show_all_nodes(), "2 11 7 9 19 3 ")
            heap_remove.remove(2)
            self.assertEqual(heap_remove.show_all_nodes(), "7 9 19 11 3 ")
            self.assertEqual(heap_remove.show_main_nodes(), "7 3 ")
            heap_remove.remove(7)
            self.assertEqual(heap_remove.show_main_nodes(), "3 9 11 ")
            self.assertEqual(heap_remove.show_all_nodes(), "3 9 19 11 ")
            heap_remove.push(12)
            heap_remove.push(22)
            heap_remove.push(6)
            heap_remove.remove(3)
            self.assertEqual(heap_remove.show_main_nodes(), "9 6 ")
            self.assertEqual(heap_remove.show_all_nodes(), "9 11 12 19 6 22 ")
            # 9       6
            # 11 19   22
            # 12
            heap_remove.remove(11)
            self.assertEqual(heap_remove.show_all_nodes(), "9 19 6 22 12 ")
            self.assertEqual(heap_remove.show_main_nodes(), "9 6 12 ")
            # 9    6   12
            # 19   22
            heap_remove.push(14)
            heap_remove.push(1)
            heap_remove.push(30)
            heap_remove.push(44)
            heap_remove.push(66)
            heap_remove.push(2)
            self.assertEqual(heap_remove.pop(), 1)
            self.assertEqual(heap_remove.show_all_nodes(), "6 12 30 44 14 9 19 22 2 66 ")
            self.assertEqual(heap_remove.show_main_nodes(), "6 2 ")
            # 6                       2
            # 12       9   22        66
            # 30 14    19
            # 44
            self.assertEqual(heap_remove.pop(), 2)
            self.assertEqual(heap_remove.show_all_nodes(), "6 12 30 44 14 9 19 22 66 ")
            self.assertEqual(heap_remove.show_main_nodes(), "6 66 ")
            self.assertEqual(heap_remove.pop(), 6)
            self.assertEqual(heap_remove.show_all_nodes(), "9 12 30 44 14 22 66 19 ")
            self.assertEqual(heap_remove.show_main_nodes(), "9 ")
            self.assertEqual(heap_remove.pop(), 9)
            self.assertEqual(heap_remove.show_all_nodes(), "12 30 44 14 22 66 19 ")
            self.assertEqual(heap_remove.show_main_nodes(), "12 22 19 ")
            self.assertEqual(heap_remove.pop(), 12)
            self.assertEqual(heap_remove.show_all_nodes(), "22 30 44 66 14 19 ")
            self.assertEqual(heap_remove.show_main_nodes(), "22 14 ")
            self.assertEqual(heap_remove.pop(), 14)
            self.assertEqual(heap_remove.show_all_nodes(), "22 30 44 66 19 ")
            self.assertEqual(heap_remove.show_main_nodes(), "22 19 ")
            self.assertEqual(heap_remove.pop(), 19)
            self.assertEqual(heap_remove.show_all_nodes(), "22 30 44 66 ")
            self.assertEqual(heap_remove.show_main_nodes(), "22 ")
            self.assertEqual(heap_remove.pop(), 22)
            self.assertEqual(heap_remove.show_all_nodes(), "30 44 66 ")
            self.assertEqual(heap_remove.show_main_nodes(), "30 66 ")
            self.assertEqual(heap_remove.pop(), 30)
            self.assertEqual(heap_remove.show_all_nodes(), "44 66 ")
            self.assertEqual(heap_remove.show_main_nodes(), "44 ")
            self.assertEqual(heap_remove.pop(), 44)
            self.assertEqual(heap_remove.show_all_nodes(), "66 ")
            self.assertEqual(heap_remove.show_main_nodes(), "66 ")
            self.assertEqual(heap_remove.pop(), 66)
            self.assertEqual(heap_remove.show_all_nodes(), "")
            self.assertEqual(heap_remove.show_main_nodes(), "")
            self.assertEqual(heap_remove.is_empty(), True)
            self.assertEqual(heap_remove.size(), 0)
if __name__ == '__main__':
    unittest.main()
