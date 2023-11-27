class Student:

        def hello(self):
            print("Hey there! I'm so excited to learn stuff.")
        
        def raise_hand(self):
            print("Pick me!")


class ChattyStudent(Student):
    
        def hello(self):
            super().hello()
            print("I'm so glad to be here with you all!")
    
        def raise_hand(self):
            for i in range(10):
                super().raise_hand()
