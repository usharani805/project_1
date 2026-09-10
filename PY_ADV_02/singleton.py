class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            print("New object created")
        return cls._instance


# Create first object
object1 = Singleton()

# Create second object
object2 = Singleton()

# Check whether both are the same
print(object1 is object2)