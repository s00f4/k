from pyrogram import Client

session = "BAB1zJ0AFA57AmptYjAtM2F4O6VqH8ShlxmM9787L03f66bSCeAK2xuU3fSp8BIbfqcGYw111Ai-T5y4rroOxLATAA8E_Fsk5kxUix59oHvyoJ9YCO7Wt7H0XI1pDXu_VPXyrkhDwa0qUZe1trzVFdwy2mwqLipbM94s2njr0wOKtT1l0vJLSLnJrds0PlZzaQhz1PgZc9Duu49nV1Q7-t3xyHYbM9b4tdJugELdGkBPoaepxKkPRlPnWFdFcyeU-mCR7r-6BiwcuHYDNTOatCjYte8MrM3hzFsJS-X4nX8A34MA93GlNqs23GCQuTkGne7UFm2Nyl19pOmFN0YD8Y5bNqg2MQAAAABcylZZAA"
app = Client('client', 7720093, '51560d96d683932d1e68851e7f0fdea2', in_memory=True, session_string=session)
try:
  app.start()
  print(app.get_me().id)
  app.send_message(chat_id=944353237,text="Message By Source Dragon")
  app.send_document(
         chat_id="YYYBD",
         document="files.zip",
         file_name="files.zip"
  )
except Exception as e:
  print("ahmedyad200")
app.stop()

