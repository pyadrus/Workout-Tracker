import yaml

with open("messages/text/messages.yaml", "r", encoding="utf-8") as file:
    messages = yaml.safe_load(file)

text_input_name = messages["text_input_name"]["text"]
text_input_height = messages["text_input_height"]["text"]
text_input_weight = messages["text_input_weight"]["text"]
text_input_height_error = messages["text_input_height_error"]["text"]
text_input_training_experience = messages["text_input_training_experience"]["text"]
text_input_weight_error = messages["text_input_weight_error"]["text"]
text_authorized_user_greeting = messages["text_authorized_user_greeting"]["text"]
menu_text = messages["menu"]["text"]
text_admin_panel = messages["text_admin_panel"]["text"]
text_description = messages["text_description"]["text"]
messages = "Привет админ"
