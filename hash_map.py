# Student: ShengTso "Andrew" Wu
# Description: Implement a hash map using Dynamic array and linked list.


# Import pre-written DynamicArray and LinkedList classes
from a5_include import *


def hash_function_1(key: str) -> int:
    """
    Sample Hash function #1 to be used with A5 HashMap implementation
    """
    hash = 0
    for letter in key:
        hash += ord(letter)
    return hash

def hash_function_2(key: str) -> int:
    """
    Sample Hash function #2 to be used with A5 HashMap implementation
    """
    hash, index = 0, 0
    index = 0
    for letter in key:
        hash += (index + 1) * ord(letter)
        index += 1
    return hash


class HashMap:
    def __init__(self, capacity: int, function) -> None:
        """
        Init new HashMap based on DA with SLL for collision resolution
        """
        self.buckets = DynamicArray()
        for _ in range(capacity):
            self.buckets.append(LinkedList())
        self.capacity = capacity
        self.hash_function = function
        self.size = 0

    def __str__(self) -> str:
        """
        Return content of hash map t in human-readable form
        """
        out = ''
        for i in range(self.buckets.length()):
            list = self.buckets.get_at_index(i)
            out += str(i) + ': ' + str(list) + '\n'
        return out

    def clear(self) -> None:
        """
        Iterate through dynamic array in hash map. If non-empty bucket found, create new linked list and
        replace bucket with new empty list. Decrement size.
        """
        for index in range(self.capacity):
            if self.buckets.get_at_index(index).length() != 0:
                length = self.buckets.get_at_index(index).length()
                self.buckets.data[index] = LinkedList()
                self.size -= length
        return

    def get(self, key: str) -> object:
        """
        If hash function is hash function 1, then send key to hash function one and get index. Calculate
        index % capacity.
        """
        if self.hash_function == hash_function_1:
            index = hash_function_1(key)
            index = index % self.capacity
        else:
            index = hash_function_2(key)
            index = index % self.capacity
        """
        If bucket at index does not contain key. If new key, add new key/value pair. If not, replace and insert.
        """
        temp =  self.buckets.get_at_index(index).contains(key)
        if temp != None:
            return temp.value
        return None

    def put(self, key: str, value: object) -> None:
        """
        If hash function is hash function 1, then send key to hash function one and get index. Calculate
        index % capacity.
        """
        if self.hash_function == hash_function_1:
            index = hash_function_1(key)
            index = index % self.capacity
        else:
            index = hash_function_2(key)
            index = index % self.capacity
        """
        If bucket at index does not contain key. If new key, add new key/value pair. If not, replace and insert.
        """
        if self.buckets.get_at_index(index).contains(key) != None:
            self.buckets.get_at_index(index).remove(key)
            self.buckets.get_at_index(index).insert(key, value)
        else:
            self.buckets.get_at_index(index).insert(key, value)
            self.size += 1
        return

    def remove(self, key: str) -> None:
        """
        If hash function is hash function 1, then send key to hash function one and get index. Calculate
        index % capacity.
        """
        if self.hash_function == hash_function_1:
            index = hash_function_1(key)
            index = index % self.capacity
        else:
            index = hash_function_2(key)
            index = index % self.capacity
        """
        Find key. Once key found, remove. If not found, return None.
        """
        if self.buckets.get_at_index(index).contains(key) != None:
            self.buckets.get_at_index(index).remove(key)
            self.size -= 1

        return None

    def contains_key(self, key: str) -> bool:
        """
        If hash function is hash function 1, then send key to hash function one and get index. Calculate
        index % capacity.
        """
        if self.hash_function == hash_function_1:
            index = hash_function_1(key)
            index = index % self.capacity
        else:
            index = hash_function_2(key)
            index = index % self.capacity
        """
        If bucket at index does contain key, return True. If not, return False.
        """
        if self.buckets.get_at_index(index).contains(key) != None:
            return True
        return False

    def empty_buckets(self) -> int:
        """
        Iterate through dynamic array. If linked list at element in array has length of 0, increment count.
        Return count.
        """
        count = 0
        for item in range(self.capacity):
            if self.buckets.get_at_index(item).length() == 0:
                count += 1
        return count

    def table_load(self) -> float:
        """
        Calculate load factor by calling size and capacity and returning results of division
        """
        return self.size / self.capacity

    def resize_table(self, new_capacity: int) -> None:
        """
        If new capacity is under 1, return. Else, create a empty hash map and add items in current
        hash map into empty hash map
        """
        if new_capacity < 1:
            return
        newHash = HashMap(self.capacity, self.hash_function)             # To create new table
        for bucket in range(self.capacity):

            temp = self.buckets.data[bucket]
            if temp.length() != 0:
                length = temp.length()
                temp = temp.head
                for link in range(length):
                    newHash.put(temp.key, temp.value)
                    temp = temp.next
        """
        Clear current hash map. Increase/decrease current hash map capacity accordingly using
        append / pop.
        """
        self.clear()
        oldCapacity = self.capacity
        capacityDelta = new_capacity - self.capacity
        if capacityDelta > 0:
            for bucket in range(capacityDelta):
                self.buckets.append(LinkedList())
                self.capacity += 1
        elif capacityDelta < 0:
            for bucket in range(abs(capacityDelta)):
                self.buckets.pop()
                self.capacity -= 1
        """
        Bring data from new hash map into current hash map
        """
        for bucket in range(oldCapacity):
            temp = newHash.buckets.data[bucket]
            if temp.length() != 0:
                length = temp.length()
                temp = temp.head
                for link in range(length):
                    self.put(temp.key, temp.value)
                    temp = temp.next
        return


    def get_keys(self) -> DynamicArray:
        """
        Create empty dynamic array for return. Iterate through buckets. When non-empty bucket reached,
        iterate through linked list and add key to return dynamic array.
        """
        returnArray = DynamicArray()
        for bucket in range(self.capacity):
            temp = self.buckets.data[bucket]
            if temp.length() != 0:
                temp = temp.head
                while temp is not None:
                    returnArray.append(temp.key)
                    temp = temp.next
        return returnArray

# BASIC TESTING
if __name__ == "__main__":

    """print("\nPDF - empty_buckets example 1")
    print("-----------------------------")
    m = HashMap(100, hash_function_1)
    print(m.empty_buckets(), m.size, m.capacity)
    m.put('key1', 10)
    print(m.empty_buckets(), m.size, m.capacity)
    m.put('key2', 20)
    print(m.empty_buckets(), m.size, m.capacity)
    m.put('key1', 30)
    print(m.empty_buckets(), m.size, m.capacity)
    m.put('key4', 40)
    print(m.empty_buckets(), m.size, m.capacity)"""


    """print("\nPDF - empty_buckets example 2")
    print("-----------------------------")
    m = HashMap(50, hash_function_1)
    for i in range(150):
        m.put('key' + str(i), i * 100)
        if i % 30 == 0:
            print(m.empty_buckets(), m.size, m.capacity)"""


    """print("\nPDF - table_load example 1")
    print("--------------------------")
    m = HashMap(100, hash_function_1)
    print(m.table_load())
    m.put('key1', 10)
    print(m.table_load())
    m.put('key2', 20)
    print(m.table_load())
    m.put('key1', 30)
    print(m.table_load())"""


    """print("\nPDF - table_load example 2")
    print("--------------------------")
    m = HashMap(50, hash_function_1)
    for i in range(50):
        m.put('key' + str(i), i * 100)
        if i % 10 == 0:
            print(m.table_load(), m.size, m.capacity)"""

    """print("\nPDF - clear example 1")
    print("---------------------")
    m = HashMap(100, hash_function_1)
    print(m.size, m.capacity)
    m.put('key1', 10)
    m.put('key2', 20)
    m.put('key1', 30)
    print(m.size, m.capacity)
    m.clear()
    print(m.size, m.capacity)"""


    """print("\nPDF - clear example 2")
    print("---------------------")
    m = HashMap(50, hash_function_1)
    print(m.size, m.capacity)
    m.put('key1', 10)
    print(m.size, m.capacity)
    m.put('key2', 20)
    print(m.size, m.capacity)
    m.resize_table(100)
    print(m.size, m.capacity)
    m.clear()
    print(m.size, m.capacity)"""

    """print("\nPDF - put example 1")
    print("-------------------")
    m = HashMap(50, hash_function_1)
    for i in range(150):
        m.put('str' + str(i), i * 100)
        #print(m.empty_buckets(), m.table_load(), m.size, m.capacity)
        if i % 25 == 24:
            print(m.empty_buckets(), m.table_load(), m.size, m.capacity)"""


    """print("\nPDF - put example 2")
    print("-------------------")
    m = HashMap(40, hash_function_2)
    for i in range(50):
        m.put('str' + str(i // 3), i * 100)
        if i % 10 == 9:
            print(m.empty_buckets(), m.table_load(), m.size, m.capacity)"""

    """print("\nPDF - contains_key example 1")
    print("----------------------------")
    m = HashMap(10, hash_function_1)
    print(m.contains_key('key1'))
    m.put('key1', 10)
    m.put('key2', 20)
    m.put('key3', 30)
    print(m.contains_key('key1'))
    print(m.contains_key('key4'))
    print(m.contains_key('key2'))
    print(m.contains_key('key3'))
    m.remove('key3')
    print(m.contains_key('key3')) """

    """print("\nPDF - contains_key example 2")
    print("----------------------------")
    m = HashMap(75, hash_function_2)
    keys = [i for i in range(1, 1000, 20)]
    for key in keys:
        m.put(str(key), key * 42)
    print(m.size, m.capacity)
    result = True
    for key in keys:
        # all inserted keys must be present
        result &= m.contains_key(str(key))
        # NOT inserted keys must be absent
        result &= not m.contains_key(str(key + 1))
    print(result)"""


    """print("\nPDF - get example 1")
    print("-------------------")
    m = HashMap(30, hash_function_1)
    print(m.get('key'))
    m.put('key1', 10)
    print(m.get('key1'))"""


    """print("\nPDF - get example 2")
    print("-------------------")
    m = HashMap(150, hash_function_2)
    for i in range(200, 300, 7):
        m.put(str(i), i * 10)
    print(m.size, m.capacity)
    for i in range(200, 300, 21):
        print(i, m.get(str(i)), m.get(str(i)) == i * 10)
        print(i + 1, m.get(str(i + 1)), m.get(str(i + 1)) == (i + 1) * 10)"""


    """print("\nPDF - remove example 1")
    print("----------------------")
    m = HashMap(50, hash_function_1)
    print(m.get('key1'))
    m.put('key1', 10)
    print(m.get('key1'))
    m.remove('key1')
    print(m.get('key1'))
    m.remove('key4') """

    """print("\nPDF - resize example 1")
    print("----------------------")
    m = HashMap(20, hash_function_1)
    m.put('key1', 10)
    print(m.size, m.capacity, m.get('key1'), m.contains_key('key1'))
    m.resize_table(30)
    print(m.size, m.capacity, m.get('key1'), m.contains_key('key1'))"""


    """print("\nPDF - resize example 2")
    print("----------------------")
    m = HashMap(75, hash_function_2)
    keys = [i for i in range(1, 1000, 13)]
    for key in keys:
        m.put(str(key), key * 42)
    print(m.size, m.capacity)


    for capacity in range(111, 1000, 117):
        m.resize_table(capacity)

        m.put('some key', 'some value')
        result = m.contains_key('some key')
        m.remove('some key')

        for key in keys:
            result &= m.contains_key(str(key))
            result &= not m.contains_key(str(key + 1))
        print(capacity, result, m.size, m.capacity, round(m.table_load(), 2))"""


    """print("\nPDF - get_keys example 1")
    print("------------------------")
    m = HashMap(10, hash_function_2)
    for i in range(100, 200, 10):
        m.put(str(i), str(i * 10))
    print(m.get_keys())
    #print("1: ", m)

    m.resize_table(1)
    print(m.get_keys())
    #print("2: ", m)

    m.put('200', '2000')
    m.remove('100')
    m.resize_table(2)
    print(m.get_keys())
    #print("3: ", m)"""
