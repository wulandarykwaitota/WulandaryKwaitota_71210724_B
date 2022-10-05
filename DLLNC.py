from NodeMahasiswa import NodeMahasiswa
class DLLNC:
    _size = 0
    _head = None
    _tail = None

    def init(self):
        self._size = 0
        self._head = None
        self._tail = None

    def len(self):
        return self._size

    def isEmpty(self):
        return self._size == 0


    def insert_head(self,nama,ipk):     
        new_node = NodeMahasiswa(nama,ipk)
        if(self.isEmpty()):
            self._head = new_node
            self._tail = new_node
            self._tail.next = None
        else:
            new_node.next = self._head
            self._head = new_node
        self._size += 1

    def deleteLast(self, position):
        if self._size == 0:
            return False
        elif position == 0:
            self.deleteLast(0)
        elif position + 1 >= self._size:
            self.deleteLast(self._size)
        else:
            delete_node = self._head
            for i in range(position):
                delete_node = delete_node.next
            helper = self._head
            while helper.next != delete_node:
                helper = helper.next
            helper.next = delete_node.next
            del delete_node
            self._size = self._size - 1  


DLLNC = doubleList()
DLLNC.addElementTail('Shalom',3.9)
DLLNC.addElementTail('Nabilla',3.8)
DLLNC.addElementTail('Kurniadi',3.7)
DLLNC.addElementtail('Hartis',3.6)
DLLNC.printDescending()

DLLNC.deleteLast()
DLLNC.printDescending()

DLLNC.raraIpk()


