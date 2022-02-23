class Phone:

    def __init__(self, number): 
        self.phone_number= number
        self.text_messages= []

    def place_call(number_to_call):
        return number_to_call

    def place_text(number_to_text, message_to_send):
        return number_to_text, message_to_send

    def save_text(message_to_save):
        return  message_to_save
    
    def get_texts():
        return

    def get_number():
        return
    

class CameraPhone(Phone):
    
    def __init__(self, phone_number):
        super().__init__(phone_number)
        self.pictures = []
        
    def take_picture(self, picture_name):
        self.pictures.append(picture_name)
        return

steve = CameraPhone(3334445555)
print(steve.phone_number)