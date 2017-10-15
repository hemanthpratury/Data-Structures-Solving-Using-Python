class Stack(object):
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, value):
        self.items.append(value)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


def balance_check(s):
    st = Stack()

    if len(s) % 2 != 0:
        return False

    for i in s:
        if i == '{' or i == '[' or i == '(':
            st.push(i)

        elif i == '}':
            if st.size() == 0 or st.peek() != '{':
                return False
            else:
                st.pop()

        elif i == ']':
            if st.size() == 0 or st.peek() != '[':
                return False
            else:
                st.pop()

        elif i == ')':
            if st.size() == 0 or st.peek() != '(':
                return False
            else:
                st.pop()

    return st.size() == 0

print(balance_check('[{({[()]})}]'))

print(balance_check('[]{}{}()[{({[]})}]'))

print(balance_check('[]{}{}()[{({[]})}]}}}))))'))