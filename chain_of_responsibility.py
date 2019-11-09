# class SomeObject:
#     def __init__(self):
#         self.integer_field = 0
#         self.float_field = 0.0
#         self.string_field = ""


class EventGet:

    def __init__(self, kind_type):
        self.kind_type = kind_type
        self.kind_value = None


class EventSet:

    def __init__(self, kind_value):
        self.kind_type = type(kind_value)
        self.kind_value = kind_value


class NullHandler:

    def __init__(self, successor=None):
        self.successor = successor

    def handle(self, some_obj, event):
        if self.successor is not None:
            return self.successor.handle(some_obj, event)


class IntHandler(NullHandler):
    def handle(self, some_obj, event):
        if event.kind_type == int:
            if event.kind_value:
                some_obj.integer_field = event.kind_value
            else:
                return some_obj.integer_field
        else:
            print("Передаю обработку дальше")
            return super().handle(some_obj, event)


class FloatHandler(NullHandler):
    def handle(self, some_obj, event):
        if event.kind_type == float:
            if event.kind_value:
                some_obj.float_field = event.kind_value
            else:
                return some_obj.float_field
        else:
            print("Передаю обработку дальше")
            return super().handle(some_obj, event)


class StrHandler(NullHandler):
    def handle(self, some_obj, event):
        if event.kind_type == str:
            if event.kind_value:
                some_obj.string_field = event.kind_value
            else:
                return some_obj.string_field
        else:
            print("Передаю обработку дальше")
            return super().handle(some_obj, event)


# obj = SomeObject()
# obj.integer_field = 42
# obj.float_field = 3.14
# obj.string_field = "some text"
# chain = IntHandler(FloatHandler(StrHandler(NullHandler())))
#
# print(chain.handle(obj, EventGet(int)))
# print(chain.handle(obj, EventGet(str)))
# print(chain.handle(obj, EventGet(int)))
# print(chain.handle(obj, EventGet(float)))
# print(chain.handle(obj, EventGet(str)))
# chain.handle(obj, EventSet(100))
# print(chain.handle(obj, EventGet(int)))
# chain.handle(obj, EventSet(0.5))
# print(chain.handle(obj, EventGet(float)))
# chain.handle(obj, EventSet('new text'))
# print(chain.handle(obj, EventGet(str)))
