class MyCalendar:

    def __init__(self):
        self.program = []

    def book(self, start: int, end: int) -> bool:
        for l in self.program:
            if start <= l[0] and end > l[0]:
                return False
            elif start >= l[1] and end < l[1]:
                return False
            elif start > l[0] and start < l[1]:
                return False
            elif end > l[0] and end < l[1]:
                return False
        self.program.append([start,end])
        return True

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
