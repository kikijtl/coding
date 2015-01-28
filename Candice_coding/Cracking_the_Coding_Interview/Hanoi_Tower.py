''' Hanoi Tower
Given 3 towers and N disks of different sizes which can slide onto any tower. At the beginning, all the N disks are sorted in ascending order
of size from top to botttom on tower 1. Write a program to move all the N disks to tower 3 with the following constraints:
(1) only one disk can be moved at a time
(2) a disk is slid off the top of one tower onto another tower
(3) a disk can only be place on top of a larget disk
Implement a program to move the disks from the first tower to the last using stacks.
'''

class Tower:
    def __init__(self, i):
        self.index = i
        self.disks = []
    def __repr__(self):
        return '%s%r' %(self.__class__.__name__, index)
    def add_disk(self, radius):
        if self.disks and self.disks[-1] <= radius:
            print 'Error.'
        else:
            self.disks.append(radius)
            
def move_disks(n, start_tower, temp_tower, dest_tower):
    if n <= 0:
        return
    move_disks(n-1, start_tower, dest_tower, temp_tower)
    '''move the top n-1 disks to the temp_tower'''
    move_bottom(start_tower, dest_tower)
    '''move the last/largest disk from start_tower to dest_tower'''
    move_disks(n-1, temp_tower, start_tower, dest_tower)
    '''move the rest n-1 disks from temp_tower to dest_tower above the largest disk'''

def move_bottom(start_tower, dest_tower):
    disk = start_tower.disks.pop()
    dest_tower.disks.append(disk)
    print 'move disk from tower%d to tower%d' %(start_tower.index, dest_tower.index)
    
if __name__ == '__main__':
    towers = [Tower(i) for i in range(3)]
    n = 3
    for i in range(n, 0, -1):
        towers[0].add_disk(i)
    move_disks(n, towers[0], towers[1], towers[2])