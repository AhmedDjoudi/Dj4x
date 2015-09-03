# coding=utf-8
#---------------------------#
# Dj4x | Jahus | 2014-07-26 #
#---------------------------#----------------------------------
# Change log
# * 2014-07-26 :
#     (1.0.0)               - first code
# * 2014-07-27 - 2014-09-30 :
#     (1.0.1 - 1.19.22)
# * 2014-10-02 :
#     (2.0.0 Bonne Jenet)   - Réécriture du code
#                           - Création des fichiers .json
#                           - Débugging
# * 2014-10-02 - 2014-10-03 :
#     (2.1.0 Bonne Jenet)   - Multiple reminders support
# * 2014-10-03 :
#     (2.1.1)               - Petite correction de foramt %
#     (2.2.1)               - Dynamisation de auto_tip
#                             et check_bal pour supporter
#                             plusieurs bots
# * 2014-10-04 :
#     (2.2.2)               - Corrections mineures
# * 2014-10-05 :
#     (2.3.2)               - Ajout de +donate
# * 2014-10-08 :
#     (2.3.3)               - Portage Python 2.7 / Linux
# * 2014-10-09 :
#     (2.3.4)               - Compatibilit? 2.7 / Linux
# * 2014-10-10 :
#     (2.3.5)               - Fixed a problem with tip timeout
# * 2014-10-15 :
#     (2.4.5)               - Added BITtrex api
#     (2.5.5)               - Unified the ticker APIs
# * 2014-10-16 :
#     (2.5.6)               - Minor fix on *ticker
# * 2014-10-22 :
#     (2.5.7)               - Minor fix on handling tips
#                             channels
# * 2014-10-23 :
#     (2.5.8)               - Arranged an oversight that
#                             prevented the bot from tipping
#                             a received tip even after a
#                             timeout or a keep <hash>
# * 2014-10-30 :
#     (2.5.9)               - Added more NOTICE messages
#                             to make the bot less spammy
#                             (addie.cc, ltcrabbit, help)
#     (2.6.9)               - Added Cryptonator API
#     (2.7.9)               - Added *convert command
#     (2.8.9)               - Added DOGED to AutoTip
# * 2014-11-09 :
#     (2.8.10)              - Fixed float division
# * 2014-11-28 :
#     (2.9.10)              - Ajouté : système de sécurité
#                             pour vérifier l'identité des
#                             administrateurs
# * 2014-12-19 :
#     (2.9.11)              - Added XPY to AutoTip
# * 2014-12-28 :
#     (2.9.12)              - Fixed: UTF-8 support for
#                             *translate and its XML parsing
# * 2014-12-29 :
#     (2.10.12)             - Added API with Chuck Norris
#                             facts (French)
# * 2015-01-02 :
#     (2.10.13)             - Ajouté +aide
# * 2015-01-06 :
#     (2.11.13)             - Ajout de la fonction de calcul
#                             à *convert
# * 2015-01-13 :
#     (2.11.14)             - Adaptation de autotip à pndtip,
#                             Tip sur le canal, non en privé.
# * 2015-01-16 :
#     (2.12.14)             - LOCAL (True|False) support
# * 2015-01-17 :
#     (2.13.14)             - Bitly API support
#                             (*bitly | *short)
# * 2015-02-01 :
#     (2.13.15)             - Minor change to LOCAL const
#                             and _timeout_reminder()
# * 2015-02-13 :
#     (2.13.16)             - Importing urllib.parse for Py3
#     (2.13.17)             - Adding "owner" params
#                             for *bitly
# * 2015-02-14 :
#     (2.13.18)             - Ajout de is_auth() pour
#                             une utilisation extérieure à
#                             cmd_admins()
#     (2.14.18)             - Remaniement de is_auth()
#                             et création de auth_users
#                             pour la gestion des
#                             groupes d'utilisateurs
# * 2015-02-16 :
#     (2.15.18)             - Ajout de api_ticker_custom()
# * 2015-02-19 :
#     (2.15.19)             - Ajout de LazyCoinsRainBot (doge)
#                             à auto-tip
# * 2015-03-14 :
#     (2.15.20)             - Version-dependent UTF-8 usage
#                             in api_chucknorrisfact()
# * 2015-08-08 :
#     (3.15.20)             - Ajout de l'interface Telegram
# * 2015-08-09 :
#     (3.16.20)             - Réglages de l'interface Telegram
# * 2015-08-10 :
#     (3.17.20)             - Ajout de la commande Telegram
#                             /enligne pour avoir la liste
#                             des utilisateurs présents sur
#                             le canal IRC.
# * 2015-08-11 :
#     (3.18.20)             - Ajout d'un filtre anti-flood
#                             pour les messages Telegram > IRC
#     (3.19.20)             - Changements de compatibilité
#                             urllib3/ssl_
#     (3.20.20)             - Ajout du transfert des messages
#                             join / part / quit
# * 2015-09-03 :
#     (3.21.20)             - UTF-8 usage in 
#                             telegram_bot_handle_message_text
#--------------------------------------------------------------
#
from __future__ import division      # Float division
#
SYSTEM = "linux" # windows | linux (see data_file)
PYTHON = 2 # 2 for 2.7 | 3 for 3.4
LOCAL = False # True: no freenode support, no tipping
              #       (for local use on local server)
			  # False: on freenode, support of tipbots,
			  #        autotips, rains, etc.
# DATA
import json
def load_file_json(file_name):
	with open(file_name, 'r') as _file:
		content = _file.read()
		content_dict = json.loads(content)
		return content_dict
# CONFIG FILES
# Windows : "D:\\Users\\Ahmed Djoudi\\AppData\\Roaming\\"
data_file = {
	"user": {
		"linux": "/root/.config/hexchat/addons/Dj4x_users.json", 
		"windows": "D:\\Users\\Ahmed Djoudi\\AppData\\Roaming\\hexchat\\addons\\Dj4x_users.json"
	}, 
	"data": {
		"linux": "/root/.config/hexchat/addons/Dj4x_data.json", 
		"windows": "D:\\Users\\Ahmed Djoudi\\AppData\\Roaming\\hexchat\\addons\\Dj4x_data.json"
	}
}
user_data = load_file_json(data_file.get("user").get(SYSTEM))
data = load_file_json(data_file.get("data").get(SYSTEM))
# MODULE INFORMATION
bot = data.get("bot")
__module_name__ = str(bot.get("name"))
__module_version__ = str("%s (%s)" % (bot.get("version"), bot.get("version_info").get("name")))
__module_description__ = str(bot.get("description"))
#
#--------------------------------------------------------------
# HEAD
#--------------------------------------------------------------
import hexchat                       # HexChat IRC client
import requests                      # API requests
import random                        # such randomness
import xml.etree.ElementTree as xET  # XML parser
import time                          # Time What Is Time, 
                                     # by Blind Guardian
# HTML parser for unescape
if PYTHON == 3:
	import html.parser as HTMLParser
	import urllib.parse as urllib_parse
else:
	import HTMLParser                # HTML parser
	import urllib as urllib_parse    # URL parser
import urllib3
urllib3.disable_warnings()
#
#--------------------------------------------------------------
# Telegram :: Classes
#--------------------------------------------------------------
#
# This object represents a Telegram user or bot.
class telegram_classes_User:
	def __init__(self, data_json):
		# id: Integer -- Unique identifier for this user or bot
		self.id = data_json.get("id")
		# first_name: String -- User's or bot's first name
		self.first_name = data_json.get("first_name")
		# last_name: String -- (Optional) User's or bot's last name
		if "last_name" in data_json:
			self.last_name = data_json.get("last_name")
		else:
			self.last_name = -1
		# user_name: String -- (Optional) User's or bot's username (without @)
		if "username" in data_json:
			self.username = data_json.get("username")
		else:
			self.username = -1
	def __str__(self):
		r_str = "User #%s | First name: %s" % (self.id, self.first_name)
		if self.last_name != -1:
			r_str += " | Last name: %s" % (self.last_name)
		if self.username != -1:
			r_str += " | Username: @%s" % (self.username)
		return r_str
#
# This object represents a group chat.
class telegram_classes_GroupChat:
	def __init__(self, data_json):
		self.id = data_json.get("id")
		self.title = data_json.get("title")
	def __str__(self):
		return "Group chat #%s: ""%s""" % (self.id, self.title)
# Types for Message
telegram_types = {
	"text": "T",
	"forward_from": "F",
	"reply_to_message": "R",
	"audio": "A",
	"document": "G",
	"photo": "I",
	"sticker": "S",
	"video": "V",
	"contact": "U",
	"location": "L",
	"new_chat_participant": "cpn",
	"left_chat_participant": "cpl",
	"new_chat_title": "ctn",
	"new_chat_photo": "cin",
	"delete_chat_photo": "cid",
	"group_chat_created": "gcc"
}
#
class telegram_classes_Message:
	def __init__(self, data_json):
		self.type = ""
		self.message_id = data_json.get("message_id")
		self.sender = telegram_classes_User(data_json.get("from"))
		self.date = data_json.get("date")
		if "title" in data_json.get("chat"):
			# GroupChat
			self.chat = telegram_classes_GroupChat(data_json.get("chat"))
		else:
			# PrivateChat (User)
			self.chat = telegram_classes_User(data_json.get("chat"))
		if "forward_from" in data_json:
			self.forward_from = telegram_classes_User(data_json.get("forward_from"))
			if telegram_types.get("forward_from") not in self.type: self.type += telegram_types.get("forward_from")
		if "forward_date" in data_json:
			self.forward_date = data_json.get("forward_date")
		if "reply_to_message" in data_json:
			self.reply_to_message = telegram_classes_Message(data_json.get("reply_to_message"))
			if telegram_types.get("reply_to_message") not in self.type: self.type += telegram_types.get("reply_to_message")
		if "text" in data_json:
			self.text = data_json.get("text")
			if telegram_types.get("text") not in self.type: self.type += telegram_types.get("text")
		if "audio" in data_json:
			self.audio = data_json.get("audio") #TODO: Audio structure
			if telegram_types.get("audio") not in self.type: self.type += telegram_types.get("audio")
		if "document" in data_json:
			self.document = data_json.get("document") #TODO: Document structure
			if telegram_types.get("document") not in self.type: self.type += telegram_types.get("document")
		if "photo" in data_json:
			self.photo = data_json.get("photo") #TODO: Photo structure
			if telegram_types.get("photo") not in self.type: self.type += telegram_types.get("photo")
		if "sticker" in data_json:
			self.sticker = data_json.get("sticker") #TODO: Sticker structure
			if telegram_types.get("sticker") not in self.type: self.type += telegram_types.get("sticker")
		if "video" in data_json:
			self.video = data_json.get("video") #TODO: Video structure
			if telegram_types.get("video") not in self.type: self.type += telegram_types.get("video")
		if "caption" in data_json:
			self.caption = data_json.get("caption")
		if "contact" in data_json:
			self.contact = data_json.get("contact") #TODO: Contact structure
			if telegram_types.get("contact") not in self.type: self.type += telegram_types.get("contact")
		if "location" in data_json:
			self.location = data_json.get("location") #TODO: Location structure
			if telegram_types.get("location") not in self.type: self.type += telegram_types.get("location")
		if "new_chat_participant" in data_json:
			self.new_chat_participant = telegram_classes_User(data_json.get("new_chat_participant"))
			if telegram_types.get("new_chat_participant") not in self.type: self.type += telegram_types.get("new_chat_participant")
		if "left_chat_participant" in data_json:
			self.left_chat_participant = telegram_classes_User(data_json.get("left_chat_participant"))
			if telegram_types.get("left_chat_participant") not in self.type: self.type += telegram_types.get("left_chat_participant")
		if "new_chat_title" in data_json:
			self.new_chat_title = data_json.get("new_chat_title")
			if telegram_types.get("new_chat_title") not in self.type: self.type += telegram_types.get("new_chat_title")
		if "new_chat_photo" in data_json:
			self.new_chat_photo = data_json.get("new_chat_photo") #TODO: Photo structure
			if telegram_types.get("new_chat_photo") not in self.type: self.type += telegram_types.get("new_chat_photo")
		if "delete_chat_photo" in data_json:
			self.delete_chat_photo = data_json.get("delete_chat_photo") # Boolean
			if telegram_types.get("delete_chat_photo") not in self.type: self.type += telegram_types.get("delete_chat_photo")
		if "group_chat_created" in data_json:
			self.group_chat_created = data_json.get("group_chat_created") # Boolean
			if telegram_types.get("group_chat_created") not in self.type: self.type += telegram_types.get("group_chat_created")
	def __str__(self):
		return "Message #%s at %s. From %s to %s." % (self.message_id, self.date, self.sender, self.chat)
#
class telegram_classes_Update:
	def __init__(self, data_json):
		self.message = telegram_classes_Message(data_json.get("message"))
		self.update_id = data_json.get("update_id")
	def __str__(self):
		return "Update #%s | %s" % (self.update_id, self.message)
#
#--------------------------------------------------------------
# Telegram :: Bot
#--------------------------------------------------------------
telegram_bot_token = data.get("telegram_params").get("token")
telegram_bot_request = "https://api.telegram.org/bot"
telegram_group_for_irc = {-18430680: "#dogecoinfrance"}
send_to_IRC = True
telegram_bifrost_enabled = False
#
telegram_bot_info = None
telegram_bot_offset = 483690311
#
def telegram_bot_get_bot_info():
	global telegram_bot_info
	req = requests.get("%s%s%s" % (telegram_bot_request, telegram_bot_token, "/getMe"))
	if (req.status_code != 200):
		print("Error %s" % req.status_code)
	else:
		req_json = req.json()
		if "ok" in req_json:
			if (req_json.get("ok") == True):
				_me = telegram_classes_User(req_json.get("result"))
				telegram_bot_info = _me
				print(telegram_bot_info)
			else:
				print("Error %s" % "There has been an unknown error")
		else:
			print("Error %s" & "There has been an unknown error.")
#
def telegram_bot_get_updates():
	global telegram_bot_offset
	# Options
	# 	offset: integer -- (Optional)
	# 	limit: integer -- (Optional)
	#   timeout: integer -- (Optional)
	req_data = {"offset": telegram_bot_offset + 1, "limit": "", "timeout": ""}
	req = requests.get("%s%s%s" % (telegram_bot_request, telegram_bot_token, "/getUpdates"), data = req_data)
	if (req.status_code != 200):
		print("Error %s" % req.status_code)
	else:
		req_json = req.json()
		# print(req_json)
		if "ok" in req_json:
			if (req_json.get("ok") == True):
				# print("-- telegram_bot_get_updates(): Got %s updates." % len(req_json.get("result")))
				for update_json in req_json.get("result"):
					_update = telegram_classes_Update(update_json)
					if _update.update_id > telegram_bot_offset: telegram_bot_offset = _update.update_id
					# Traiter le message reçu
					telegram_bot_read_message(_update.message)
			else:
				print("-- telegram_bot_telegram_get_updates(): Error %s" % "There has been an unknown error")
		else:
			print("-- telegram_bot_get_updates(): Error %s" & "There has been an unknown error.")
#
def telegram_bot_send_message(chat_id, text, reply_to_message_id = None, reply_markup = None):
	# Options
	#	chat_id
	#	text
	#	disable_web_page_preview
	#	reply_to_message_id
	#	reply_markup
	head_data = {
		"chat_id": chat_id,
		"text": text
	}
	if reply_to_message_id != None:
		head_data.update([("reply_to_message_id", reply_to_message_id)])
	if reply_markup != None:
		head_data.update([("reply_markup", reply_markup)])
	# print("-- send_message(): head_data = %s" % head_data)
	#
	req = requests.post(url = "%s%s%s" % (telegram_bot_request, telegram_bot_token, "/sendMessage"), data = head_data)
	if (req.status_code != 200):
		print("-- send_message(): Error %s" % req.status_code)
	else:
		req_json = req.json()
		# print(req_json)
		#TODO: Verify if send message is equal to received message
#
def telegram_bot_read_message(message):
	# print("reading message %s" % message.message_id)
	# Checking message type
	if telegram_types.get("text") in message.type:
		telegram_bot_handle_message_text(message)
	elif telegram_types.get("new_chat_participant") in message.type:
		telegram_bot_handle_message_chat_participant_new(message)
	elif telegram_types.get("left_chat_participant") in message.type:
		telegram_bot_handle_message_chat_participant_left(message)
	elif telegram_types.get("new_chat_title") in message.type:
		telegram_bot_handle_message_chat_title_new(message)
	elif telegram_types.get("group_chat_created") in message.type:
		telegram_bot_handle_message_group_chat_created(message)
	else:
		print("-- read_message(): Message type unhandled")
#
def telegram_bot_handle_message_text(message):
	_to = ""; _from = ""
	_text = message.text
	if message.sender.id != message.chat.id:
		_to = "@%s" % message.chat.title
	if telegram_types.get("forward_from") in message.type:
		_from = " [fwd: %s]" % message.forward_from.first_name
		if _text[0] == "<":
			_from = " [fwd: %s]" % _text[1:].split(">")[0]
			_text = ' '.join(_text[1:].split(">")[1:])[1:]
	if PYTHON == 2:
		print(("[#%s]\t<%s%s%s> %s" % (message.message_id, message.sender.first_name, _to, _from, message.text)).encode("UTF-8"))
	else:
		print("[#%s]\t<%s%s%s> %s" % (message.message_id, message.sender.first_name, _to, _from, message.text))
	# Telegram bridge (to IRC)
	_multi_line_text = message.text.split('\n')
	# Anti-flood system:
	if len(_multi_line_text) > 4:
		_multi_line_text = _multi_line_text[:min(3, len(_multi_line_text))]
		_multi_line_text.append("[... and more on Telegram.]")
		print(_multi_line_text)
	if (not telegram_bifrost_enabled) and (message.chat.id in telegram_group_for_irc):
		current_context = hexchat.find_context(channel = telegram_group_for_irc.get(message.chat.id))
		if _text[0] in data.get("triggers_all"):
			triggers_manager(_text[0], message.sender, current_context, _text, _text[1:].split())
		for _line in _multi_line_text:
			current_context.command(("msg %s <%s%s> %s" % (current_context.get_info("channel"), message.sender.first_name, _from, _line)).encode("UTF-8"))
	#
	# Handle commands
	# user / chat / command / arguments(full_text)
	if len(_text) > 2 and _text[0] == "/":
		if _to == "":
			# Privé
			_command = _text[1:].split()[0]
			_args = _text[1:].split()[1:]
			print("-- Private command is: %s | With args: %s" % (_command, _args))
			telegram_bot_command_user(_command, _args, message.sender, message.message_id)
		elif ("@" + telegram_bot_info.username.lower()) in _text.lower():
			# Groupe + Hilight
			# /command@Dj4xBot
			_bot_username = _text[1:].split('@')[1][:len(telegram_bot_info.username)].lower()
			print("_bot_username = %s" % _bot_username)
			if _bot_username.lower() == telegram_bot_info.username.lower():
				_command = _text[1:].split('@')[0]
				_args = (" ".join(_text[1:].split('@')[1:])[len(_bot_username):]).split()
				print("-- Group command is: %s | With args: %s" % (_command, _args))
				telegram_bot_command_user(_command, _args, message.sender, message.message_id, message.chat)
		else:
			# Group /without hilight
			# /command [args]
			_command = _text[1:].split()[0]
			_args = _text[1:].split()[1:]
			print("-- Group command is: %s | With args: %s" % (_command, _args))
			telegram_bot_command_user(_command, _args, message.sender, message.message_id, message.chat)
#
def telegram_bot_handle_message_chat_participant_new(message):
	print("[#%s]\t** %s joined group %s" % (message.message_id, message.new_chat_participant.first_name, message.chat.title))
	if message.new_chat_participant.id != telegram_bot_info.id:
		telegram_bot_send_message(message.chat.id, "Hello, %s." % message.new_chat_participant.first_name, reply_to_message_id = message.message_id)
	else:
		telegram_bot_send_message(message.chat.id, "Salut tout le monde ! [chat #%s]" % message.chat.id, message.message_id)
def telegram_bot_handle_message_chat_participant_left(message):
	print("[#%s]\t** %s left group %s" % (message.message_id, message.left_chat_participant.first_name, message.chat.title))
	if message.left_chat_participant.id != telegram_bot_info.id:
		telegram_bot_send_message(message.chat.id, "Bye, %s." & message.left_chat_participant.first_name, reply_to_message_id = message.message_id)
def telegram_bot_handle_message_chat_title_new(message):
	print("[#%s]\t** Group %s changed title to ""%s""" % (message.message_id, message.chat.id, message.new_chat_title))
def telegram_bot_handle_message_group_chat_created(message):
	print("[#%s]\t** Group chat ""%s"" created" % (message.message_id, message.chat.title))
	telegram_bot_send_message(message.chat.id, "Salut tout le monde !")
def telegram_bot_handle_message_audio(message):
	print("Sorry, I can't hear audio for now.")
def telegram_bot_handle_message_document(message):
	print("Sorry, I can't download files for now.")
def telegram_bot_handle_message_picture(message):
	print("Sorry, I can't see pictures for now.")
def telegram_bot_handle_message_sticker(message):
	print("Sorry, I don't care about stickers for now.")
def telegram_bot_handle_message_video(message):
	print("Sorry, I can't watch videos for now.")
def telegram_bot_handle_message_contact(message):
	print("Sorry, I have nothing to do with this contact for now.")
def telegram_bot_handle_message_location(message):
	print("Sorry, I can't change location, nor look at it for now.")
def telegram_bot_handle_message_chat_photo_new(message):
	print("Sorry, I can't see chat photos for now.")
def telegram_bot_handle_message_chat_photo_delete(message):
	print("Sorry, I don't care about photos for now.")
#
def telegram_bot_telegram_bot_command_start(context):
	# Démarre le bot
	print("Started!")
def telegram_bot_command_about(context, original_message_id):
	# Fournit le texte d'à propos
	telegram_bot_send_message(context, "@Dj4xBot\nDj4x version 3.15.20\nPar @Jahus\nUtilisez /aide pour avoir la liste des commandes.", original_message_id)
def telegram_bot_command_user(msg, args, user, original_message_id, chat = None):
	if chat == None: chat = user
	cmd = msg.split()[0]
	# print("Received command '%s' with arguments '%s'." % (cmd, args))
	# telegram_bot_send_message(chat.id, "Received command '%s' with arguments '%s'." % (cmd, args), original_message_id)
	if cmd.lower() == "about":
		telegram_bot_command_about(chat.id, original_message_id)
	if cmd.lower() == "enligne":
		get_irc_channel_users(user, chat, original_message_id)
	if cmd.lower() == "keskifichou":
		telegram_bot_send_message(chat.id, "Une vraie chaudasse !", original_message_id)
#
# get_bot_info()
# get_updates()
print("EoF@offset: %s" % telegram_bot_offset)
#
#--------------------------------------------------------------
# CONSTANTES
#--------------------------------------------------------------
hexchat_format = {
	"bold": "\002", 
	"colour": "\003", 
	"hidden": "\010", 
	"underline": "\037", 
	"original": "\017", 
	"reverse_colour": "\026", 
	"beep": "\007", 
	"italics": "\035"
}
units = {
	"btc": {
		"name": "Bitcoin", 
		"short": "BTC", 
		"submultiple": "SAT"
	}, 
	"ltc": {
		"name": "Litcoin", 
		"short": "LTC", 
		"submultiple": "LIT"
	}
}
about = "%s version %s, by Jahus." % (__module_name__, __module_version__)
help_header = {
	"about": {
		"descr": [
			"> +about", 
			("  \- %s" % about)
		]
	}, 
	"help": {
		"descr": [
			"> %(help)shelp [command|all]" % data.get("triggers"), 
			"  |- help: Lists all the commands supported by the bot.", 
			"  |- help all: Returns help on all commands (could be spamy).", 
			"  \- help <command>: Returns help on the given command."
		]
	}, 
}
help_api = {
	"balance": {
		"descr": ["> %(api)sbalance <address>" % data.get("triggers"), "  |- Gives the balance on an address.", "  \- Supported: DOGE | PND."]
	}, 
	"pandapool": {
		"descr": ["> %(api)spandapool <algo> <address>" % data.get("triggers"), "  |- Gives live stats on the workers for Pandapool.", "  |- Gives history from the last three rounds.", "  |- <algo> : Scrypt | X11.", "  \- Pandapool address: multi.pandapool.info"]
	}, 
	"hashfaster": {
		"descr": ["> %(api)shashfaster doge <api_key>" % data.get("triggers"), "  |- Gives live stats for a user from Hashfaster.", "  \- Supported: DOGE."]
	}, 
	"block": {
		"descr": ["> %(api)sblock" % data.get("triggers"), "  |- Info on the blockchain:", "   |- last solved block difficulty,", "   |- remaining blocks until next halvening,", "   |- time until next halvening.", "  \- Supported: DOGE."]
	}, 
	"unscramble": {
		"descr": ["> %(api)sunscramble <word>" % data.get("triggers"), "  |- Returns unscrambled word for the given word's letters.", "  \- Supported: English."]
	}, 
	"addie": {
		"descr": ["> %(api)saddie <nick> [opt <coin>]" % data.get("triggers"), "  |- Returns the <coin> address for <user> as on Addie.cc service.", "  |- If no <coin> argument: returns all addresses for <user> on Addie.cc service.", "  \- If no arguments, searches for all addresses for current user on Addie.cc service."]
	}, 
	"ltcrabbit": {
		"descr": ["> %(api)sLTCrabbit <API_key> [full/exchange]" % data.get("triggers"), "  |- Returns information for an account from LTCrabbit.", "  |- Shows balance and worker information.", "  |- [full]: Displays pool statistics, user balance, workers and last three rounds payout.", "  |- [exchange]: Displays LTC and BTC exchange rates (in USD and EUR) as given by LTCrabbit.", "  \- Pool: ltcrabbit.com"]
	},
	"translate": {
		"descr": ["> %(api)stranslate <from> <to> <text>" % data.get("triggers"), "  |- Translates <text> from a language to another using Microsoft Translation systems.", "  \- For language codes, see Translator Language Codes on MSDN: http://msdn.microsoft.com/en-us/library/hh456380.aspx"]
	}, 
	"ticker": {
		"descr": ["> %(api)sticker <coin>" % data.get("triggers"), "  |- Gives the ticker in BTC (or SAT) for a coin.", "  \- Gets information from Bter, BITtrex and Mintpal."]
	}, 
	"chuck": {
		"descr": ["> %(api)schuck [tri] [type]" % data.get("triggers"), "  |- Renvoie une Chuck Norris fact à partir de http://chucknorrisfacts.fr/.", "  |- [type] peut être %(bold)stxt%(bold)s (text) ou %(bold)simg%(bold)s (image)." % hexchat_format, "  |- [tri] peut être : %(bold)slast%(bold)s (la plus récente), %(bold)sfirst%(bold)s (la plus ancienne), %(bold)stop%(bold)s (la mieux notée), %(bold)sflop%(bold)s (la moins bien notée), %(bold)smtop%(bold)s (la mieux notée en moyenne), %(bold)smflop%(bold)s (la moins bien notée en moyenne), %(bold)salea%(bold)s (aléatoire)" % hexchat_format, "  \- Les valeurs par défaut sont %(bold)stxt%(bold)s et %(bold)salea%(bold)s." % hexchat_format]
	}, 
	"bitly": {
		"descr": ["> %(api)sbitly <longURL>" % data.get("triggers"), "  \- Shorten a link from Bitly"]
	}
}
#
#--------------------------------------------------------------
# Commands
#--------------------------------------------------------------
get_msg = {
	bot.get("cmd_default").get("msg_trig"): {
		"words": bot.get("cmd_default").get("msg_txt") % hexchat_format, 
		"descr": ["> %s" % bot.get("cmd_default").get("msg_descr")]
	}, 
	"morito": {
		"words": data.get("morito"), 
		"descr": ["> %(users)smorito" % data.get("triggers"), "  \- Ever wanted to know how to make a morito?"]
	}, 
	"diablo": {
		"words": data.get("diablo"), 
		"descr": ["> %(users)sdiablo" % data.get("triggers"), "  \- Ever wanted to know how to make a diablo?"]
	}, 
	"aide": {
		"words": data.get("irchelp-fr") % hexchat_format, 
		"descr": ["> %(users)saide" % data.get("triggers"), "  \- Affiche le lien d'aide IRC : https://gist.github.com/AhmedDjoudi/bbbad10fad9e52eb22cc"]
	}
}
get_action = {
	bot.get("cmd_default").get("action_trig"): {
		"words": bot.get("cmd_default").get("action_words"), 
		"suppl": [bot.get("cmd_default").get("action_suppl") % hexchat_format], 
		"descr": [bot.get("cmd_default").get("action_descr")]
	}, 
	"lick": {
		"words": ["lick", "licks"], 
		"suppl": ["'s hand", "'s mouth", "'s eye"], 
		"reason_no": "He's scary!", 
		"descr": ["> %(users)slick [opt <nick>]" % data.get("triggers"), "  \- Licks the user or someone who is present on the channel."]
	}, 
	"hug": {
		"words": ["hug", "hugs"], 
		"suppl": [""], 
		"reason_no": "He's thorny!", 
		"descr": ["> %(users)shug [opt <nick>]" % data.get("triggers"), "  \- Hugs the user or someone who is present on the channel."]
	}, 
		"sleep": {
		"words": ["sleep with", "sleeps with"], 
		"suppl": [". wow", ". such hot", ". many soft"], 
		"reason_no": "He's fat!", 
		"descr": ["> %(users)slick [opt <nick>]" % data.get("triggers"), "  \- Licks the user or someone who is present on the channel."]
	}, 
	"cocktail": {
		"words": ["serve", "serves"], 
		"suppl": [" a morito", " a diablo"], 
		"reason_no": "He's already drunk and stone!", 
		"descr": ["> %(users)scocktail [opt <nick>]" % data.get("triggers"), "  \- Serves a cocktail to the user or a person on the channel."]
	},
	"vend": {
		"words": ["vend", "vends"], 
		"suppl": (data.get("vend") % hexchat_format).split(" // "), 
		"reason_no": "He doesn't need to dig!", 
		"descr": ["> %(users)svend [opt <nick>]" % data.get("triggers"), "  \- Vends something to the user or a person on the channel."]
	}, 
	"dick": {
		"words": ["dick", "dicks"], 
		"suppl": ["'s mouth", "'s pussy"], 
		"reason_no": "Ooow, no!", 
		"descr": ["> %(users)sdick [opt <nick>]" % data.get("triggers"), " \- Dicks the user or someone who is present on the channel."]
	}
}
get_reaction = {
	"wof": "wof! wof!",
	"thx-1138": "THX-1138!"
}
help = {
	"About the bot (%(help)s)" % data.get("triggers"): help_header, 
	"Messages      (%(users)s)" % data.get("triggers"): get_msg, 
	"Actions       (%(users)s)" % data.get("triggers"): get_action, 
	"Functions     (%(api)s)" % data.get("triggers"): help_api
}
#
#--------------------------------------------------------------
# VARIABLES
#--------------------------------------------------------------
DOGE_BLOCK = 31250
balance = {
	"doger": "0", 
	"pndtip": "0", 
	"dogewallet": "0", 
	"dogedshibebot": "0", 
	"xpytip": "0", 
	"lazycoinsrainbot": "0"
}
message_bal = {
	"doger": 0, 
	"pndtip": 0, 
	"dogewallet": 0, 
	"dogedshibebot": 0, 
	"xpytip": 0, 
	"lazycoinsrainbot": 0
}
message_bal_context = None
ms_token = ""
ms_token_timout = 0
ms_token_last_sync = 0
tips = {}
tips_waiting_amount = 0
#
del bot
#
#--------------------------------------------------------------
# IDENTIFYING
#--------------------------------------------------------------
#
# MODULE LAUNCH MESSAGE
auth_users = data.get("auth_users")
for admin in auth_users.get("admins"):
	hexchat.command("msg %s %s started" % (admin, __module_name__))
#
# IDENTIFICATION WITH FREENODE
def ident():
	current_nick = hexchat.get_info("nick")
	if hexchat.nickcmp(current_nick, __module_name__) != 0:
		hexchat.command("msg NickServ REGAIN %s" % (__module_name__))
		hexchat.command("msg NickServ RECOVER %s" % (__module_name__))
		hexchat.command("nick %s" % (__module_name__))
#
ident()
#
#--------------------------------------------------------------
# HOOKS
#--------------------------------------------------------------
#
# Channel messsages
def trig_chan(word, word_eol, userdata):
	# Strip input word
	for i in range(len(word)):
		word[i] = hexchat.strip(word[i], -1, 3)
	#
	user = word[0]
	trig = word[1][0]
	msg_no_trigger = word[1][1:]
	msg_full = word[1].lower()
	# Splits the words to get command and args
	words = (word[1][1:].strip()).split(' ')
	# Hence:
	#   words[0] : command
	#   words[1:] : arguments
	#
	current_context = hexchat.get_context()
	#
	auto_tip(user, current_context, words)
	#
	triggers_manager(trig, telegram_classes_User({"id": -1, "first_name": user}), current_context, msg_full, words)
	for wrd in get_reaction:
		if wrd.lower() in msg_full:
			current_context_command_msg_chan(current_context, get_reaction.get(wrd.lower()))
	# Telegram bridge
	if (current_context.get_info("channel").lower() in data.get("telegram_params").get("channels")) and not telegram_bifrost_enabled:
		telegram_bot_send_message(data.get("telegram_params").get("channels").get(current_context.get_info("channel").lower()), "<%s> %s" % (user, word[1]))
	return hexchat.EAT_NONE
# Hooks the function to "Channel Message" event
hexchat.hook_print("Channel Message", trig_chan)
#
# Hilight in channels
def trig_hilight(word, word_eol, userdata):
	# STRIP word
	for i in range(len(word)):
		word[i] = hexchat.strip(word[i], -1, 3)
	#
	user = word[0]
	trig = word[1][0]
	msg_no_trigger = word[1][1:]
	msg_full = word[1].lower()
	# Splits the words to get command and args
	words = (word[1][1:].strip()).split(' ')
	# words[0] : command
	# words[1:] : arguments
	#
	current_context = hexchat.get_context()
	# Rain
	rain_params = data.get("rain_params")
	if (user.lower() in rain_params.get("bots")):
		_tipped(user, current_context, msg_full)
	# Telegram bridge
	if (current_context.get_info("channel").lower() in data.get("telegram_params").get("channels")) and not telegram_bifrost_enabled:
		telegram_bot_send_message(data.get("telegram_params").get("channels").get(current_context.get_info("channel").lower()), "<%s> %s" % (user, word[1]))
#
hexchat.hook_print("Channel Msg Hilight", trig_hilight)
#
# Personal message
def trig_pm(word, word_eol, userdata):
	global balance
	global message_bal
	
	# Strip the input word
	for i in range(len(word)):
		word[i] = hexchat.strip(word[i], -1, 3)
	#
	user = word[0]
	msg_full = word[1].lower()
	trig = word[1][0]
	words = (word[1][1:].strip()).split(' ')
	# Hence:
	#   words[0] : command
	#   words[1:] : arguments
	#
	current_nick = hexchat.get_info("nick")
	current_context = hexchat.get_context()
	#
	rain_params = data.get("rain_params")
	if (user.lower() in rain_params.get("bots")) and ("tipped you" in msg_full):
		_tipped(user, current_context, msg_full)
	#
	if (user.lower() == "doger") and ("balance is".lower() in msg_full):
		if PYTHON > 2:
			msg_bal = msg_full.split()[4][1:]
		else:
			msg_bal = msg_full.split()[4][2:]
		balance.update([("doger", msg_bal)])
		if (message_bal.get("doger") == 1):
			current_context_command_msg_chan(message_bal_context, "my current Dogecoin balance is: '%s' DOGE" % ((int(balance.get("doger")) - tips_waiting_amount)))
			message_bal.update([("doger", 0)])
	if (user.lower() == "pndtip") and (("%s has" % current_nick).lower() in msg_full):
		msg_bal = msg_full.split()[2]
		balance.update([("pndtip", msg_bal)])
		if (message_bal.get("pndtip") == 1):
			current_context_command_msg_chan(message_bal_context, "my current Pandacoin balance is: '%s' PND" % (balance.get("pndtip")))
			message_bal.update([("pndtip", 0)])
	if (user.lower() == "dogedshibebot") and (("%s has" % current_nick).lower() in msg_full):
		msg_bal = msg_full.split()[2]
		balance.update([("dogedshibebot", msg_bal)])
		if (message_bal.get("dogedshibebot") == 1):
			current_context_command_msg_chan(message_bal_context, "my current Dogecoindark balance is: '%s' DOGED" % (balance.get("dogedshibebot")))
			message_bal.update([("dogedshibebot", 0)])
	if (user.lower() == "dogewallet") and ("Balance:".lower() in msg_full):
		msg_bal = msg_full.split()[2]
		balance.update([("dogewallet", msg_bal)])
		if (message_bal.get("dogewallet") == 1):
			current_context_command_msg_chan(message_bal_context, "my current Dogecoin balance on DogeWallet is: '%s' DOGE" % (balance.get("dogewallet")))
			message_bal.update([("dogewallet", 0)])
	if (user.lower() == "xpytip") and ("Balance".lower() in msg_full):
		msg_bal = msg_full.split()[4]
		balance.update([("xpytip", msg_bal)])
		if (message_bal.get("xpytip") == 1):
			current_context_command_msg_chan(message_bal_context, "my current Paycoin balance on XPYtip is: '%s' PAYTOSHI" % (balance.get("xpytip")))
			message_bal.update([("xpytip", 0)])
	if (user.lower() == "lazycoinsrainbot") and (("%s has" % current_nick).lower() in msg_full):
		msg_bal = msg_full.split()[2]
		balance.update([("lazycoinsrainbot", msg_bal)])
		if (message_bal.get("lazycoinsrainbot") == 1):
			current_context_command_msg_chan(message_bal_context, "my current LazyCoinsRainBot balance is: '%s' DOGE" % (balance.get("lazycoinsrainbot")))
			message_bal.update([("lazycoinsrainbot", 0)])
	#
	if (msg_full.split(' '))[0] in data.get("tip_manage_commands"):
		tip_manage_auth(user, current_context, msg_full)
	return hexchat.EAT_NONE
# Hooks the function to "Private Message to Dialog" event
hexchat.hook_print("Private Message to Dialog", trig_pm)
#
def trig_user_join(word, word_eol, userdata):
	print("-- trig_user_join(): word = '%s'" % word)
	user_nick = word[0]
	channel = word[1]
	user_host = word[2]
	# Telegram bridge
	if (channel.lower() in data.get("telegram_params").get("channels")) and (not telegram_bifrost_enabled):
		telegram_bot_send_message(data.get("telegram_params").get("channels").get(channel.lower()), "** %s (%s) has joined %s" % (user_nick, user_host, channel))
hexchat.hook_print("Join", trig_user_join)
#
def trig_user_part(word, word_eol, userdata):
	print("-- trig_user_part(): word = '%s'" % word)
	user_nick = word[0]
	user_host = word[1]
	channel = word[2]
	# Telegram bridge
	if (channel.lower() in data.get("telegram_params").get("channels")) and (not telegram_bifrost_enabled):
		telegram_bot_send_message(data.get("telegram_params").get("channels").get(channel.lower()), "** %s (%s) has left %s" % (user_nick, user_host, channel))
hexchat.hook_print("Part", trig_user_part)
#
def trig_user_quit(word, word_eol, userdata):
	print("-- trig_user_quit(): word = '%s'" % word)
	user_nick = word[0]
	user_quit_reason = word[1]
	user_host = word[2]
	channel = hexchat.get_context().get_info("channel")
	print("-- trig_user_quit(): channel = %s" % channel)
	# Telegram bridge
	if (channel.lower() in data.get("telegram_params").get("channels")) and (not telegram_bifrost_enabled):
		telegram_bot_send_message(data.get("telegram_params").get("channels").get(channel.lower()), "** %s (%s) has quit (Reason: %s)" % (user_nick, user_host, user_quit_reason))
hexchat.hook_print("Quit", trig_user_quit)
#
# STORE FOUND IP
ip_dict = dict()
#
def found_ip(word, word_eol, userdata):
	# STRIP word
	for i in range(len(word)):
		word[i] = hexchat.strip(word[i], -1, 3)
	current_context = hexchat.get_context()
	server_str = current_context.get_info("server")
	server_strs = server_str.split(".")
	server_name = server_strs[1].lower()
	ip_dict.update([(server_name, word[0])])
	return hexchat.EAT_NONE
# Hooks the function to "Found IP" event
hexchat.hook_print("Found IP", found_ip)
#
#--------------------------------------------------------------
# auto_tip
#--------------------------------------------------------------
def auto_tip(user, context, cmd):
	mult = 10
	#tip
	tip_exclude = data.get("tip_params").get("tip_ban")
	tip_channels = data.get("tip_params").get("tip_channels")
	if (user.lower() not in tip_exclude) and ((context.get_info("channel")).lower() in tip_channels):
		if (len(cmd) > 2):
			_rnd = random.uniform(0, 100)
			_proba = tip_channels.get((context.get_info("channel")).lower())[2]
			if (_rnd <= _proba):
				min = tip_channels.get((context.get_info("channel")).lower())[0]
				max = min * mult
				_coin = tip_channels.get((context.get_info("channel")).lower())[1]
				_bot = tip_channels.get((context.get_info("channel")).lower())[3]
				if "." in balance.get(_bot):
					bal_parts = (balance.get(_bot)).split(".")
					_bal = bal_parts[0]
				else:
					_bal = balance.get(_bot)
				if (_bot == "doger"):
					margin = tips_waiting_amount
				else:
					margin = 0
				if (int(_bal) > max + margin):
					tip = int(random.uniform(min, max)) + 1
					if _bot in [tip_channels.get("#pandacoinpnd")[3]]:
						current_context_command_msg_chan(context, "!tip %s %s %s, \002yay!!!\002 [random tip | overall proba: %s%% | tip me to keep going!]" % (user, tip, _coin, _proba*len(tip_channels)))
					else:
						current_context_command_msg_user(context, _bot, "tip %s %s" % (user, tip))
						context.command("me tipped %s %i %s, yay!!! [random tip | overall proba: %s%% | tip me to keep going!]" % (user, tip, _coin, _proba*len(tip_channels)))
					# update balance
					check_bal("Dj4x", None, "checkbal", [_bot])
				else:
					context.command("me was going to tip %s but hasn't enough %s. (%s)" % (user, _coin.upper(), int(_bal)))
					current_context_command_msg_chan(context, "I tip speaking people randomly, tip me %s to keep it going." % (_coin.upper()))
#
#--------------------------------------------------------------
# UNLOAD
#--------------------------------------------------------------
def unload_me(userdata):
	for admin in auth_users.get("admins"):
		hexchat.command("msg %s %s unloaded" % (admin, __module_name__))
	print("EoF@offset: %s" % telegram_bot_offset)
	return hexchat.EAT_NONE
hexchat.hook_unload(unload_me)
#
#--------------------------------------------------------------
# TIMERS
#--------------------------------------------------------------
timer = None
timer_first = None
timer_timout = data.get("timer_timout")
timer_first_timout = data.get("timer_first_timout")
#
def _timout(userdata):
	global timer_first
	ident()
	if not LOCAL:
		check_bal("Dj4x", None, "checkbal", [])
	# stops the first timer
	if timer_first is not None:
		hexchat.unhook(timer_first)
		timer_first = None
	# hexchat.command("msg Jahus ping")
	return 1 # keep going
#
timer = hexchat.hook_timer(timer_timout*1000, _timout)
timer_first = hexchat.hook_timer(timer_first_timout*1000, _timout)
#
timer_tip = None
tip_timeout = data.get("tip_timeout")
#
def _timout_tip(userdata):
	global tips
	global tips_waiting_amount
	tips_tmp = tips.copy()
	for tip in tips:
		_time = (tips.get(tip)).get("time")
		if (time.time() > (_time + tip_timeout)):
			print("Tip [%s] timed out by %s s" % (tip, (time.time() - (_time + tip_timeout))))
			print("Reducing the tip amount (%s) from tip_waiting_amount." % tips.get(tip).get("amount"))
			tips_waiting_amount -= tips.get(tip).get("amount")
			print("Deleting tip [%s] from the list." % (tip))
			del tips_tmp[tip]
	tips = tips_tmp.copy()
	return 1
#
timer_tip = hexchat.hook_timer(tip_timeout*1000, _timout_tip)
#
# Cleaning variables
del timer_timout
del timer_first_timout
#
# other timers
reminders = data.get("reminders")
for reminder in reminders:
	if (reminders.get(reminder).get("local") == LOCAL):
		def _timeout_reminder(userdata, reminder=reminder):
			for _channel in reminders.get(reminder).get("channels"):
				hexchat.command("msg %s %s" % (_channel, reminders.get(reminder).get("message") % hexchat_format))
			return 1
		hexchat.hook_timer(reminders.get(reminder).get("timeout")*1000, _timeout_reminder)
	#reminders.update(
	#	[
	#		(reminder, {
	#				"channels": reminders.get(reminder).get("channels"), 
	#				"hook": hexchat.hook_timer(reminders.get(reminder).get("timeout")*1000, _timeout_reminder), 
	#				"timeout": reminders.get(reminder).get("timeout"), 
	#				"message": reminders.get(reminder).get("message")
	#			}
	#		)
	#	]
	#)
timer_telegram = None
timer_telegram_first = None
timer_telegram_timeout = data.get("telegram_params").get("timeout")
timer_telegram_timeout_first = data.get("telegram_params").get("timeout_first")
#
def _timeout_telegram(userdata):
	if timer_telegram_first is None:
		try:
			telegram_bot_get_updates()
		except:
			print("** Telegram interface :: Can't get updates | Error from _timeout_telegram()")
	return 1
timer_telegram = hexchat.hook_timer(timer_telegram_timeout*1000, _timeout_telegram)
#
def _timeout_telegram_first(userdata):
	global timer_telegram_first
	try:
		telegram_bot_get_bot_info()
	except:
		print("** Telegram interface :: Can't get bot info | Error from script call to telegram_bot_get_bot_info()")
	hexchat.unhook(timer_telegram_first)
	timer_telegram_first = None
	return 1
timer_telegram_first = hexchat.hook_timer(30*1000, _timeout_telegram_first)
#
#--------------------------------------------------------------
# Hubs
#--------------------------------------------------------------
def cmd_users_sp(user, context, cmd, args):
	user_type = "users_sp"
	global waiting_msg
	chan = context.get_info("channel")
	# Waiting message
	#if (cmd.lower() == "message"):
	#	message = ("No waiting message for now, %s" % (user))
	#	if (len(args) == 0):
	#		if (waiting_msg != ""): message = waiting_msg
	#		hexchat.command("msg %s %s" % (chan, message))
	#	else:
	#		waiting_msg = "Waiting message from %s: %s" % (user, ' '.join(args[0:]))
	# Get channels
	_channels = user_data.get("Jahus").get("channels")
	if is_auth(user, context, users_type):
		if (cmd.lower() == "channels") and (user in auth_users.get("admins")):
			if (len(args) > 2):
				hexchat.command("msg %s Too many args for %s command." % (user, cmd))
			if (len(args) == 2):
				if args[0].lower() not in _channels:
					hexchat.command("msg %s Can't find the server %s in the database." % (user, args[0]))
				else:
					if args[1].lower() not in ["join", "part"]:
						hexchat.command("msg %s Bad argument '%s' for %s command." % (user, args[1], cmd))
					else:
						for channel in _channels.get(args[0].lower()):
							hexchat.command("msg %s %%%s %s" % (chan, args[1], channel))
			if (len(args) == 1):
				if args[0].lower() not in _channels:
					hexchat.command("msg %s Can't find the server %s in the database." % (user, args[0]))
				else:
					hexchat.command("msg %s Channels found for %s on database:" % (chan, args[0]))
					for channel in _channels.get(args[0].lower()):
						hexchat.command("msg %s - %s" % (chan, channel))
			if (len(args) == 0):
				server_str = context.get_info("server")
				server_strs = server_str.split(".")
				server = server_strs[1]
				for channel in _channels.get(server):
						hexchat.command("msg %s - %s" % (chan, channel))
		# Get ip
		if (cmd.lower() == "ip"):
			get_ip(user, chan, cmd, args)
	else:
		print("*** cmd_users_sp() authentification failed. Handeled by is_auth(%s)" % user_type)
#
def cmd_users(user, context, msg, words):
	chan = context.get_info("channel")
	cmd = words[0]
	args = words[1:]
	# GET_ACTION
	if (cmd.lower() in get_action):
		do_action(user, context, cmd, args, get_action.get(cmd.lower()).get("words"), get_action.get(cmd.lower()).get("suppl"), get_action.get(cmd.lower()).get("reason_no"))
	# GET_MSG
	if (cmd.lower() in get_msg):
		# do_cmd(user, context, "msg", ("%s %s" % (chan, (get_msg.get(cmd.lower())).get("words"))).split(' '))
		current_context_command_msg_chan(context, (get_msg.get(cmd.lower())).get("words"))
	# GET about
	if (cmd.lower() == "about"):
		current_context_command_msg_chan(context, about)
	# CHECK BAL
	if (cmd.lower() == "dj4xbal"):
		check_bal(user, context, cmd, args)
	# DONATE
	if (cmd.lower() == "donate"):
		current_context_command_msg_chan(context, "If you like the bot and want to donate, send Dogecoin to: %s" % (get_user_data(data.get("bot").get("name"), "donation")))
	# TIP MANAGEMENT
	if (cmd.lower() in data.get("tip_manage_commands")):
		tip_manage_auth(user, context, msg[1:])
	# rain : active
	if (cmd.lower() == "active"):
		rain_users = get_rain_users(context)
		if rain_users == None:
			hexchat.command("msg %s Beware. There was a WTF ERROR." % chan)
		else:
			context.command("me remembers %i active users." % len(rain_users))
#
def is_auth(user, context, user_type):
	chan = context.get_info("channel")
	cc_users = context.get_list("users")
	for i in cc_users:
		if (i.nick.lower() == user.lower()):
			if i.account.lower() in auth_users.get(user_type):
				return True
			else:
				current_context_command_msg_chan(context, "Please, %s (account: '%s'), stop \002\00304impersonating\003\002!" % (user, i.account))
				for admin in auth_users.get(user_type):
					if admin != user.lower():
						current_context_command_msg_chan(context, "\002\00304SECURITY ALERT!\003\002 User '%s' on account '%s' is trying to impersonate one of you, Masters!" % (user, i.account))
				return False
#
def cmd_admins(user, context, msg, words):
	user_type = "admins"
	chan = context.get_info("channel")
	cmd = words[0]
	args = words[1:]
	cc_users = context.get_list("users")
	if is_auth(user, context, user_type):
		if (cmd.lower() == "do"):
			if (len(args) < 2):
				context.command("msg %s ERROR: Not enough arguments to make a command." % chan)
			else:
				do_cmd(user, context, args[0], args[1:])
	else:
		print("*** cmd_admins(): Admin command fail. Handeled by is_auth(%s)" % user_type)
#
def cmd_api(user, context, cmd, args):
	chan = context.get_info("channel")
	# Bitly shortener
	if (cmd.lower() in ["bitly", "short"]):
		api_bitly(user, context, cmd, args)
	# Chuck Norris facts
	if (cmd.lower() == "chuck"):
		api_chucknorrisfact(user, context, cmd, args)
	# ColdCryptos info
	if (cmd.lower() == "info"):
		if len(args) != 1:
			hexchat.command("msg %s ERROR: not enough arguments for command '%s'." % (user, cmd))
		else:
			_msg = (api_coldcryptos("info", args[0].lower(), "N/A")).split("\n")
			for _line in _msg:
				hexchat.command("msg %s %s" % (chan, _line))
	# BALANCE CHECK
	if (cmd.lower() == "balance"):
		if (args[0][0] not in ["D", "P"]):
			# invalid address
			hexchat.command("msg %s The address in not a Dogecoin address, nor a Pandacoin PND address." % (chan))
		else:
			if (args[0][0] == "D"): api_dogechain_bal(user, chan, cmd, args)
			if (args[0][0] == "P"): api_pandacoin_bal(user, chan, cmd, args)
	# HashFaster STATS
	if (cmd.lower() == "hashfaster"):
		api_hashfaster(user, chan, cmd, args)
	# PANDAPOOL STATS
	if (cmd.lower() == "pandapool"):
		api_pandapool(user, chan, cmd, args)
	# DOGECHAIN INFO
	if (cmd.lower() in ["block", "halvening"]):
		api_dogechain_info(user, chan, cmd, args)
	# UNSCRABMLE
	if (cmd.lower() == "unscramble"):
		api_unscramble(user, chan, cmd, args)
	# ADDIE.CC
	if (cmd.lower() == "addie"):
		api_addie_cc(user, chan, cmd, args)
	# LTCrabbit
	if (cmd.lower() == "ltcrabbit"):
		api_ltc_rabbit(user, chan, cmd, args)
	# BING translation
	if (cmd.lower() == "translate"):
		api_translate(user, chan, cmd, args)
	# TICKER
	if (cmd.lower() == "ticker"):
		api_ticker(user, context, cmd, args)
	# CONVERT
	if (cmd.lower() == "convert"):
		api_convert_coin(user, context, cmd, args)
#
#--------------------------------------------------------------
# FUNCTIONS
#--------------------------------------------------------------
#
# me <act> <user> [suppl] [reason]
def do_action(user, context, cmd, args, action, suppl, reason):
	chan = context.get_info("channel")
	suppl_i = int(random.uniform(0, len(suppl)))
	if (len(args) == 0):
		context.command("me %s %s%s." % (action[1], user, suppl[suppl_i]))
	if (len(args) > 0):
		cc_users = context.get_list("users")
		if (args[0].lower() == "ChanServ".lower()):
			if reason == "": reason == "scary"
			hexchat.command("msg %s Sorry, %s, I cannot %s %s%s. %s" % (chan, user, action[0], "ChanServ", suppl[suppl_i], reason))
		else:
			found = 0
			for i in cc_users:
				if (i.nick.lower() == args[0].lower()):
					context.command("me %s %s%s." % (action[1], i.nick, suppl[suppl_i]))
					found = 1
			if (found != 1):
				# Makes the action on present users only
				hexchat.command("msg %s Sorry, %s, I cannot %s %s. I can't find them here." % (chan, user, action[0], args[0]))
				#context.command("me %s %s%s." % (action[1], ' '.join(args[0:]), suppl[suppl_i]))
def do_cmd(user, context, cmd, args):
	if (len(args) < 1):
		context.command("msg %s Error: not enough arguments to send a message." % context.get_info("channel"))
	else:
		context.command("%s %s" % (cmd.lower(), ' '.join(args)))
#
def check_bal(user, context, cmd, args):
	global message_bal
	global message_bal_context
	if context != None:
		chan = context.get_info("channel")
	else:
		chan = ""
		context = hexchat.get_context()
	# TO-DO: AUTOMATE THIS PROCEDURE
	#        Seriously, it's getting hilarious!
	check_doger = 1
	check_pndtip = 1
	check_dogewallet = 1
	check_dogedshibebot = 1
	check_xpytip = 1
	check_lazycoinsrainbot = 1
	if (len(args) > 1):
		hexchat.command("msg %s Too many args for %s" % (user, cmd))
	if (len(args) == 1):
		if (args[0].lower() == "doger"):
			check_pndtip = 0
			check_dogewallet = 0
			check_dogedshibebot = 0
			check_xpytip = 0
			check_lazycoinsrainbot = 0
		if (args[0].lower() == "pndtip"):
			check_doger = 0
			check_dogewallet = 0
			check_dogedshibebot = 0
			check_xpytip = 0
			check_lazycoinsrainbot = 0
		if (args[0].lower() == "dogewallet"):
			check_doger = 0
			check_pndtip = 0
			check_dogedshibebot = 0
			check_xpytip = 0
			check_lazycoinsrainbot = 0
		if (args[0].lower() == "doge"):
			check_pndtip = 0
			check_dogedshibebot = 0
			check_xpytip = 0
		if (args[0].lower() == "pnd"):
			check_doger = 0
			check_dogewallet = 0
			check_dogedshibebot = 0
			check_xpytip = 0
			check_lazycoinsrainbot = 0
		if (args[0].lower() == "doged"):
			check_doger = 0
			check_pndtip = 0
			check_dogewallet = 0
			check_xpytip = 0
			check_lazycoinsrainbot = 0
		if (args[0].lower() == "dogedshibebot"):
			check_doger = 0
			check_pndtip = 0
			check_dogewallet = 0
			check_xpytip = 0
			check_lazycoinsrainbot = 0
		if (args[0].lower() == "xpy"):
			check_doger = 0
			check_pndtip = 0
			check_dogewallet = 0
			check_dogedshibebot = 0
			check_lazycoinsrainbot = 0
		if (args[0].lower() == "xpytip"):
			check_doger = 0
			check_pndtip = 0
			check_dogewallet = 0
			check_dogedshibebot = 0
			check_lazycoinsrainbot = 0
		if (args[0].lower() == "lazycoinsrainbot"):
			check_doger = 0
			check_pndtip = 0
			check_dogewallet = 0
			check_dogedshibebot = 0
			check_xpytip = 0
	if (len(args) == 0):
		check_doger = 1
		check_pndtip = 1
		check_dogewallet = 1
		check_dogedshibebot = 1
		check_xpytip = 1
		check_lazycoinsrainbot = 1
	if (check_doger == 1):
		context.command("msg %s balance" % "doger")
		if (chan != ""):
			message_bal_context = context
			message_bal.update([("doger", 1)])
	if (check_pndtip == 1):
		context.command("msg %s balance" % "pndtip")
		if (chan != ""):
			message_bal_context = context
			message_bal.update([("pndtip", 1)])
	if (check_dogewallet == 1):
		context.command("msg %s balance" % "dogewallet")
		if (chan != ""):
			message_bal_context = context
			message_bal.update([("dogewallet", 1)])
	if (check_dogedshibebot == 1):
		context.command("msg %s balance" % "dogedshibebot")
		if (chan != ""):
			message_bal_context = context
			message_bal.update([("dogedshibebot", 1)])
	if (check_xpytip == 1):
		context.command("msg %s balance" % "xpytip")
		if (chan != ""):
			message_bal_context = context
			message_bal.update([("xpytip", 1)])
	if (check_lazycoinsrainbot == 1):
		context.command("msg %s balance" % "lazycoinsrainbot")
		if (chan != ""):
			message_bal_context = context
			message_bal.update([("lazycoinsrainbot", 1)])
#
# Get ip
def get_ip(user, chan, cmd, args):
	if (len(args) > 1):
		hexchat.command("msg %s Too many args for %s command." % (user, cmd))
	else:
		server = "n/a"
		if (len(args) == 1):
			server = args[0].lower()
		if (len(args) == 0):
			# Gets the current context
			current_context = hexchat.get_context()
			server_str = current_context.get_info("server")
			server_strs = server_str.split(".")
			server = server_strs[1]
		if (server == "n/a"):
			hexchat.command("msg %s There were an error processing the command %s on args %s." % (user, cmd, args))
		else:
			if (server == "all"):
				hexchat.command("msg %s All ips stored in my memory:" % (user))
				for server in ip_dict:
					hexchat.command("msg %s - %s used for %s" % (user, ip_dict.get(server), server))
			else:
				if (server in ip_dict):
					server_ip = ip_dict.get(server)
					hexchat.command("msg %s IP used to connect to %s is: %s" % (user, server, server_ip))
				else:
					hexchat.command("msg %s No ip found for server %s in my memory." % (user, server))
#
# Help
def get_help(user, context, cmd, args):
	chan = context.get_info("channel")
	user_name = user.first_name
	if (len(args) > 1):
		current_context_command_msg_chan(context, "Too many args for %s command, %s." % (cmd, user_name))
	else:
		if (len(args) == 0):
			current_context_command_msg_user(context, user, about)
			current_context_command_msg_user(context, user, "Here's a list of my commands, use the trigger %s on channels:" % (data.get("triggers").get("users")))
			# sending the list
			for cmd_group in help:
				cmd_names = help.get(cmd_group).keys()
				current_context_command_msg_user(context, user, "- %s: %s" % (cmd_group, (', ').join(cmd_names)))
			# informing the channel and the user
			current_context_command_msg_chan(context, "I sent you a message with a list of my commands, %s." % (user_name))
		else:
			# searching for the command
			if (args[0].lower() == "all"):
				current_context_command_msg_chan(context, "%s" % (about))
				current_context_command_msg_chan(context, "Here's a list of my commands with their full description as you asked on %s:" % (chan))
				# sending the whole help text
				for cmd_group in help:
					current_context_command_msg_chan(context, "%s:" % (cmd_group))
					for cmd_name in help.get(cmd_group):
						cmd_descr = help.get(cmd_group).get(cmd_name).get("descr")
						for cmd_descr_line in cmd_descr:
							current_context_command_msg_chan(context, "%s" % (cmd_descr_line))
				# informing the user
				current_context_command_msg_chan(context, "I sent you a message with a list of my commands, %s." % (user_name))
			else:
				found = 0
				for cmd_group in help:
					if (args[0].lower() in help.get(cmd_group)):
						found = 1
						cmd_descr = help.get(cmd_group).get(args[0].lower()).get("descr")
				if found == 1:
					descr_len = len(cmd_descr)
					if (descr_len < 3):
						current_context_command_msg_chan(context, "Help for '%s' as asked by %s:" % (args[0].lower(), user_name))
						for cmd_descr_line in cmd_descr:
							current_context_command_msg_chan(context, "%s" % (cmd_descr_line))
					else:
						current_context_command_msg_chan(context, "Help for '%s' as asked by %s sent in notice." % (args[0].lower(), user_name))
						for cmd_descr_line in cmd_descr:
							context.command("NOTICE %s %s" % (user_name, cmd_descr_line))
				else:
					current_context_command_msg_chan(context, "Sorry, %s, the command '%s' doesn't exist." % (user_name, args[0]))
#
def api_translate_get_token(user, chan, cmd, args):
	global ms_token_timout
	global ms_token_last_sync
	global ms_token
	current_time = time.time()
	ms_params = data.get("ms_params")
	if ((current_time - ms_token_last_sync) > ms_token_timout):
		req_data = {"client_id": ms_params.get("ms_client_id"), "client_secret": ms_params.get("ms_client_secret"), "scope": ms_params.get("ms_scope"), "grant_type": ms_params.get("ms_grant_type")}
		# req_data = urllib.parse.urlencode({...})
		req = requests.post("https://datamarket.accesscontrol.windows.net/v2/OAuth2-13", data = req_data)
		req_dict = req.json()
		ms_token = req_dict.get("access_token")
		ms_token_timout = float(req_dict.get("expires_in"))
		hexchat.command("msg Jahus Generated a new token. Times out in: %.2fs" % (ms_token_timout))
		ms_token_last_sync = time.time()
		hexchat.command("msg Jahus Token: %s" % ms_token)
		return ms_token
	else:
		hexchat.command("msg Jahus The old token is just fine. Generated %.2fs ago. Will expire in %.2fs." % ((current_time - ms_token_last_sync), (ms_token_timout - (current_time - ms_token_last_sync))))
		return ms_token
#
def api_translate(user, chan, cmd, args):
	current_context = hexchat.get_context()
	if (len(args) < 3):
		hexchat.command("msg %s Sorry, %s, not enough arguments for %s." % (chan, user, cmd))
	else:
		# DATA TO TRANSLATE
		l_from = args[0]
		l_to = args[1]
		t_text = ' '.join(args[2:])
		req_data = {"text": t_text, "from": l_from, "to": l_to}
		ms_language = data.get("ms_params").get("ms_language")
		if (l_from in ms_language) and (l_to in ms_language):
			# OAUTH TOKEN
			token = api_translate_get_token(user, chan, cmd, args)
			auth_token = "Bearer %s" % token
			head_data = {"Authorization": auth_token}
			# REQUEST
			req = requests.get(url = ("http://api.microsofttranslator.com/v2/Http.svc/Translate?text=%s&from=%s&to=%s" % (t_text, l_from, l_to)), headers = head_data)
			if (req.status_code != 200):
				hexchat.command("msg %s There was an error on your request, %s (ERROR %s)." % (chan, user, req.status_code))
			else:
				req_xml = req.text
				# version 2.9.11 > 2.9.12
				x_parser = xET.XMLParser(encoding="UTF-8")
				x_parser.feed(req_xml.encode("UTF-8"))
				x_root = x_parser.close()
				x_string = x_root.text.encode("UTF-8")
				# Old, but fixed thanks to ChrisWarrick
				#> x_root = xET.fromstring(req_xml.encode("utf-8"))
				#> x_string = x_root.text.encode("utf-8") #.find("string").text
				# Thanking Microsoft:
				# current_context.command("me (thanks to Microsoft) is translating from '%s' to '%s' for %s:" % (ms_language.get(l_from), ms_language.get(l_to), user))
				hexchat.command("msg %s %s" % (chan, x_string))
		else:
			if (l_from.lower() not in ms_language):
				hexchat.command("msg %s %s is an unrecognised language, %s." % (chan, l_from, user))
			if (l_to.lower() not in ms_language):
				hexchat.command("msg %s %s is an unrecognised language, %s." % (chan, l_to, user))
#
def api_ltc_rabbit(user, chan, cmd, args):
	stuff = "ltcrabbit"
	if (len(args) > 2):
		hexchat.command("msg %s Sorry, too many arguments for %s." % (user, cmd))
	else:
		compact = 1
		exchange = 0
		if (len(args) == 2):
			if (args[1].lower() in ["full", "exchange"]):
				if args[1].lower() == "full": compact = 0
				if args[1].lower() == "exchange": exchange = 1
			else:
				hexchat.command("msg %s Sorry, bad argument '%s' for %s. All info will be displayed." % (user, args[1], user))
		if (args[0].lower() == "me"):
			user_d = get_user_data(user, stuff)
			if (user_d != ""): args[0] = user_d
		req = requests.get("https://www.ltcrabbit.com/index.php?page=api&action=getappdata&appname=general&appversion=1&api_key=%s" % (args[0]))
		if (req.status_code != 200):
			hexchat.command("msg %s There was an error on your request, %s (ERROR %s)." % (chan, user, req.status_code))
		else:
			# print(req.json())
			req_json = req.json()
			req_data = req_json.get("getappdata")
			# print(req_data)
			if compact == 1:
				hexchat.command("msg %s Information from LTCrabbit as requested by %s:" % (chan, user))
			if exchange == 1:
				hexchat.command("msg %s Exchange information from LTCrabbit as requested by %s:" % (chan, user))
			if (exchange == 0) and (compact == 0):
				hexchat.command("msg %s Information from LTCrabbit pool for user under API key %s as requested by %s:" % (chan, '...'.join([args[0][:3], args[0][len(args[0])-3:]]), user))
			if ("general" in req_data) and (compact == 0) and (exchange == 0):
				ltc_rabbit_general = req_data.get("general")
				if (ltc_rabbit_general.get("message") != ""):
					hexchat.command("msg %s - Message from the pool: %s" % (chan, ltc_rabbit_general.get("message")))
			if ("pool" in req_data) and (compact == 0) and (exchange == 0):
				ltc_rabbit_pool = req_data.get("pool")
				hexchat.command("msg %s LTC/day per MH/s :: Scrypt: %s LTC | X11 %s LTC" % (chan, ltc_rabbit_pool.get("ltc_mh_scrypt"), ltc_rabbit_pool.get("ltc_mh_x11")))
				hexchat.command("msg %s Hashrate :: Scrypt: %.2f MH/s | X11: %.2f MH/s" % (chan, float(ltc_rabbit_pool.get("hashrate_scrypt"))/1000, float(ltc_rabbit_pool.get("hashrate_x11"))/1000))
			if ("ltc_exchange_rates" in req_data) and (compact == 0):
				ltc_rates = req_data.get("ltc_exchange_rates")
				hexchat.command("msg %s LTC EXCH :: %s USD | %s EUR" % (chan, ltc_rates.get("USD"), ltc_rates.get("EUR")))
			if ("btc_exchange_rates" in req_data) and (compact == 0):
				btc_rates = req_data.get("btc_exchange_rates")
				hexchat.command("msg %s BTC EXCH :: %s USD | %s EUR" % (chan, btc_rates.get("USD"), btc_rates.get("EUR")))
			if ("user" in req_data) and (exchange == 0):
				ltc_rabbit_user = req_data.get("user")
				hexchat.command("msg %s User: %s | Balance: %.8f" % (chan, ltc_rabbit_user.get("username"), ltc_rabbit_user.get("balance")))
				hexchat.command("msg %s Scrypt: %.2f kH/s (%.2f%% invalid) | X11: %.2f kH/s (%.2f%% invalid)" % 
					(chan, 
					ltc_rabbit_user.get("hashrate_scrypt"), 
					ltc_rabbit_user.get("invalid_shares_scrypt"), 
					ltc_rabbit_user.get("hashrate_x11"), 
					ltc_rabbit_user.get("invalid_shares_x11")))
			if ("worker" in req_data) and (exchange == 0):
				ltc_rabbit_workers = req_data.get("worker")
				if (len(ltc_rabbit_workers) == 0):
					hexchat.command("msg %s No workers found." % (chan))
				for worker in ltc_rabbit_workers:
					active = "inactive"
					if worker.get("active") == 1: active = "active"
					hexchat.command("NOTICE %s Worker %s: %.2f kH/s | %s | Algo: %s" % (user, worker.get("name"), worker.get("hashrate"), active, worker.get("algo")))
			if ("earnings" in req_data) and (compact == 0) and (exchange == 0):
				ltc_earn_basis = (req_data.get("earnings")).get("basis")
				if len(ltc_earn_basis) == 0:
					hexchat.command("msg %s No payout history found." % (chan))
				else:
					hexchat.command("NOTICE %s Payout for last %s rounds:" % (user, min(3, len(ltc_earn_basis))))
					for i in range(min(3, len(ltc_earn_basis))):
						j = (len(ltc_earn_basis) - 1) - i
						hexchat.command("NOTICE %s Payout %s : %.8f LTC" % (user, ltc_earn_basis[j].get("timestamp"), ltc_earn_basis[j].get("amount")))
			if (exchange == 1):
				hexchat.command("msg %s Please, next time, don't use me to see the exchange information alone. Check with the other bots." % (user))
#
# ADDIE.CC
def api_addie_cc(user, chan, cmd, args):
	adi_wiki = "fr.wikipedia.org/wiki/Adi_(personnage)"
	if (len(args) > 2):
		hexchat.command('msg %s Adi dit: "Non, %s, pas comme รงa!" Pour en savoir plus: %s' % (chan, user, adi_wiki))
	else:
		if (len(args) == 2):
			if (args[1].lower() != "all"):
				req = requests.get("http://addie.cc/api/%s/%s" % (args[0], args[1]))
				if (req.status_code != 200):
					hexchat.command("msg %s There's no such user or no %s address for %s" % (chan, args[1], args[0]))
				else:
					req_text = req.text
					# print(req.text)
					hexchat.command("msg %s %s address for %s as requested by %s: %s" % (chan, args[1], args[0], user, req_text))
			else:
				username = args[0]
				api_addie_cc_all(user, chan, cmd, args, username)
		if (len(args) == 1):
			username = args[0]
			api_addie_cc_all(user, chan, cmd, args, username)
		if (len(args) == 0):
			username = user
			api_addie_cc_all(user, chan, cmd, args, username)
#
def api_addie_cc_all(user, chan, cmd, args, username):
	req = requests.get("http://addie.cc/api/%s" % (username))
	if (req.status_code != 200):
		hexchat.command("msg %s There's no such user (error %s)" % (chan, req.status_code))
	else:
		req_dict = req.json()
		if (len(req_dict) == 0):
			hexchat.command("msg %s There are no addresses on profile %s." % (chan, username))
		elif (len(req_dict) < 3):
			hexchat.command("msg %s All addresses for %s on Addie.cc as requested by %s:" % (chan, username, user))
			for coin in req_dict:
				# print(coin)
				req_coin = req_dict.get(coin)
				# print(req_coin)
				hexchat.command("msg %s - %s: %s" % (chan, coin, req_dict.get(coin)))
		else:
			hexchat.command("msg %s All addresses for %s on Addie.cc as requested by %s sent in notice." % (chan, username, user))
			for coin in req_dict:
				# print(coin)
				req_coin = req_dict.get(coin)
				# print(req_coin)
				hexchat.command("NOTICE %s - %s: %s" % (user, coin, req_dict.get(coin)))
#
# Unscramble
def api_unscramble(user, chan, cmd, args):
	if (len(args) != 1):
		hexchat.command("msg %s You know why %s can't work this way, %s." % (chan, cmd, user))
	else:
		req = requests.get("http://www.scrambledwordsolver.com/solver.cgi?word=%s" % (args[0]))
		req_text = req.text
		req_split = req_text.split('>')
		found = 0
		# print(req_split)
		for i in range(len(req_split)):
			if (req_split[i] == "<li"):
				if ((req_split[i+1].rstrip("</ul")).rstrip("\n") == "Sorry, no word could be found.\n".rstrip("\n")):
					found = 0
				else:
					found = 1
					hexchat.command("msg %s Unscrambled %s for %s: %s" % (chan, args[0], user, req_split[i+2].rstrip("</a")))
		if (found == 0): hexchat.command("msg %s Sorry, %s, can't find unscrambled word for %s." % (chan, user, args[0]))
#
# Pandacoin PND address
def api_pandacoin_bal(user, chan, cmd, args):
	chain = "pandacoin"
	if (len(args) != 1):
		hexchat.command("msg %s You know why %s can't work this way, %s." % (chan, cmd, user))
	else:
		req = requests.get("http://pandachain.net/chain/PandaCoin/q/addressbalance/%s" % (args[0]))
		req_bal = req.text
		current_context = hexchat.get_context()
		current_context.command("me found %.8f PND at address %s as asked by %s (according to pandachain.net)." % (float(req_bal), args[0], user))
#
# DOGECHAIN BAL
def api_dogechain_bal(user, chan, cmd, args):
	if (len(args) != 1):
		hexchat.command("msg %s You know why %s can't work this way, %s." % (chan, cmd, user))
	else:
		req = requests.get("http://dogechain.info/api/v1/address/balance/%s" % args[0])
		req_dict = req.json()
		req_len = len(req_dict)
		if (req_len != 2):
			hexchat.command("msg %s Don't ask me why, %s, but there was an error with your %s request (unexpected, of course)." % (chan, user, cmd))
		else:
			req_success = req_dict.get("success")
			if (req_success == 1):
				current_context = hexchat.get_context()
				current_context.command("me found %.8f DOGE at address %s as asked by %s (according to DogechainAPI)." % (float(req_dict.get("balance")), args[0], user))
			else:
				hexchat.command("msg %s Sorry, %s, DogechainAPI answered with an error: %s" % (chan, user, req_dict.get("error")))
#
# DOGECHAIN INFO
def api_dogechain_info(user, chan, cmd, args):
	if (len(args) != 0):
		hexchat.command("msg %s Too much arguments for a command like %s." % (chan, cmd))
	else:
		req = requests.get("http://dogechain.info/chain/Dogecoin/q/getblockcount")
		req_block = req.text
		print("req_block = %s" % req_block)
		remaining_blocks = ((int(int(req_block)/100000)+1)*100000) - int(req_block)
		print("remaining_blocks = %s" % remaining_blocks)
		hexchat.command("msg %s Current block: %s." % (chan, req_block))
		hexchat.command("msg %s Blocks until next halvening: %s." % (chan, remaining_blocks))
		years_bis = float(remaining_blocks / (60*24*365))
		years = int(years_bis)
		print("years_bis = %s | years = %s" % (years_bis, years))
		months_bis = float(((years_bis - years)*365)/30)
		months = int(months_bis)
		print("months_bis = %s | months = %s" % (months_bis, months))
		days_bis = float(((months_bis - months)*30))
		days = int(days_bis)
		print("days_bis = %s | days = %s" % (days_bis, days))
		hours_bis = float(((days_bis - days)*24))
		hours = int(hours_bis)
		print("hours_bis = %s | hours = %s" % (hours_bis, hours))
		minutes = int((hours_bis - hours)*60)
		print("minutes = %s" % minutes)
		print("y: %s m: %s d: %s h: %s mn: %s" % (years, months, days, hours, minutes))
		halvening_time = ""
		# print('"%s"' % halvening_time)
		if (years != 0):
			p_y = ""
			if years > 1: p_y = "s"
			halvening_time = ("%s %s year%s" % (halvening_time, years, p_y))
		if (months != 0):
			p_m = ""
			if months > 1: p_m = "s"
			halvening_time = ("%s %s month%s" % (halvening_time, months, p_m))
		if (days != 0):
			p_d = ""
			if days > 1: p_d = "s"
			halvening_time = ("%s %s day%s" % (halvening_time, days, p_d))
		if (hours != 0):
			halvening_time = ("%s %s h" % (halvening_time, hours))
		if (minutes != 0):
			halvening_time = ("%s %s mn" % (halvening_time, minutes))
		hexchat.command("msg %s Time until next halvening:%s." % (chan, halvening_time))
#
# HashFaster STATS
def api_hashfaster(user, chan, cmd, args):
	stuff = "hashfaster"
	if (len(args) != 2):
		hexchat.command("msg %s You know why %s command can't work this way, %s." % (chan, cmd, user))
	else:
		if (args[0].lower() not in ["doge"]):
			hexchat.command("msg %s Sorry, %s, bad arguments for %s." % (chan, user, cmd))
		else:
			if (args[1] == "me"):
				user_d = get_user_data(user, stuff)
				if (user_d != ""): args[1] = user_d
			req = requests.get("https://%s.hashfaster.com/index.php?page=api&action=getuserstatus&api_key=%s" % (args[0], args[1]))
			if (req.status_code != 200):
				hexchat.command("msg %s ERROR %s" % (chan, req.status_code))
			else:
				req_dict = req.json()
				req_len = len(req_dict)
				if (req_len == 0):
					hexchat.command("msg %s ERROR" % (chan))
				else:
					req_user = req_dict.get("getuserstatus")
					req_data = req_user.get("data")
					if "username" in req_data:
						hexchat.command("msg %s User: %s" % (chan, req_data.get("username")))
					if "hashrate" in req_data:
						hexchat.command("msg %s Hashrate: %.2f" % (chan, req_data.get("hashrate")))
					if "sharerate" in req_data:
						expected = (float(req_data.get("sharerate"))/100)*DOGE_BLOCK
						hexchat.command("msg %s Round payout: %.8f DOGE" % (chan, expected))
					if "shares" in req_data:
						req_shares = req_data.get("shares")
						hexchat.command("msg %s Shares: (%s valid | %s invalid)" % (chan, req_shares.get("valid"), req_shares.get("invalid")))
#
# PANDAPOOL STATS
def api_pandapool(user, chan, cmd, args):
	stuff = "pandapool"
	if (len(args) != 2):
		hexchat.command("msg %s You know why %s command can't work this way, %s." % (chan, cmd, user))
	else:
		if (args[0].lower() not in ["scrypt", "x11"]):
			hexchat.command("msg %s Sorry, %s, bad arguments for %s." % (chan, user, cmd))
		else:
			if (args[1] == "me"):
				user_d = get_user_data(user.lower(), stuff)
				if (user_d != -1): args[1] = user_d
			if (args[0].lower() == "scrypt"):
				req = requests.get("http://multi.pandapool.info/api.php?q=userinfo&user=%s" % args[1])
			else:
				req = requests.get("http://multi.pandapool.info/api.php?q=userinfo&algo=x11&user=%s" % args[1])
			# continue
			req_dict = req.json()
			req_len = len(req_dict)
			if (req_len != 2):
				hexchat.command("msg %s Don't ask me why, %s, but there was an error with your %s request (unexpected, of course)." % (chan, user, cmd))
			else:
				req_error = req_dict.get("error")
				if (req_error == 1):
					hexchat.command("msg %s Sorry, %s, PandapoolAPI answered with an error: %s." % (chan, user, req_dict.get("msg")))
				else:
					req_results = req_dict.get("result")
					req_res_len = len(req_results)
					if (req_res_len > 2):
						hexchat.command("msg %s Don't ask me why, %s, but there was an error with your %s request (unexpected, of course)." % (chan, user, cmd))
					else:
						# RESULTS
						hexchat.command("msg %s Results from Pandapool for %s with %s:" % (chan, args[0], args[1]))
						# UNIT
						if (args[1][0] == "P"):
							unit = "PND"
						if (args[1][0] == "D"):
							unit = "DOGE"
						if ("workers" not in req_results):
							hexchat.command("msg %s No live info." % (chan))
						else:
							# WORKERS
							req_live_workers = req_results.get("workers")
							for i in req_live_workers:
								hexchat.command("msg %s Worker: %s | difficulty: %s | hashrate: %s kH/s" % (chan, i[0], i[1], i[2]))
						if ("history" not in req_results):
							hexchat.command("msg %s No history." % (chan))
						else:
							# HISTORY
							req_history = req_results.get("history")
							if (len(req_history) == 0):
								hexchat.command("msg %s No history to show." % (chan))
							else:
								hexchat.command("notice %s History for last rounds:" % user)
								for i in range(min(3, len(req_history))):
									c_round = req_history[i]
									c_round_nbr = c_round.get("round")
									c_round_pay = c_round.get("payout")
									c_round_workers = c_round.get("workers")
									if (len(c_round_workers) > 1):
										s = "s"
									else:
										s = ""
									hexchat.command("notice %s Round: %s | Payout: %.8f %s | With %s worker%s" % (user, c_round_nbr, float(c_round_pay), unit, len(c_round_workers), s))

#
def get_user_data(user, stuff):
	found = 0
	for _user in user_data:
		_user_data = user_data.get(_user)
		if (user.lower() in _user_data.get("nicks")):
			if stuff in _user_data.get("data"):
				return _user_data.get("data").get(stuff)
				found = 1
	if (found == 0): return -1
#
def _tipped(user, context, msg):
	global tips
	args = (msg.strip()).split(' ')
	tip_update = 1
	if "you" in args:
		print("Handling private message...")
		tip_hash = args[11][1:9]
		tip_source = args[1].lower()
		if PYTHON > 2:
			tip_amount = int(args[5][1:])
		else:
			tip_amount = int(args[5][2:])
		tip_time = time.time()
	elif "much" in args:
		print("Handling channel message...")
		tip_hash = args[12][1:9]
		tip_source = args[1].lower()
		if PYTHON > 2:
			tip_amount = int(args[4][1:])
		else:
			tip_amount = int(args[4][2:])
		tip_time = time.time()
	else:
		print("ERROR: can't handle the tip.")
		tip_update = -1
	if tip_hash in tips:
		print("Tip %s already saved, checking..." % tip_hash)
		tip_channel = ((tips.get(tip_hash)).get("context")).get_info("channel")
		if tip_channel[0] == "#":
			print("Tip %s already saved, found from channel %s, no update needed." % (tip_hash, tip_channel))
			tip_update = 0
	else:
		print("Tip %s is not on memory. Adding..." % tip_hash)
		tip_update = 2
	if (tip_update > -1):
		tip_account = get_account_(tip_source, context)
		_tip = {
			tip_hash: {
				"source": tip_source, 
				"account": tip_account, 
				"amount": tip_amount, 
				"context": context,
				"time": time.time(), 
				"bot": user.lower()
			}
		}
	if (tip_update > 0):
		print("Updating/adding tip %s..." % tip_hash)
		tips.update(_tip)
		print("Done!")
	if (tip_update == 2):
		tip_query(tip_hash)
#
def tip_query(hash):
	global tips_waiting_amount
	print("Querrying tip %s..." % hash)
	_message = []
	_tip = tips.get(hash)
	_amount = _tip.get("amount")
	print("Increasing the tips_waiting_amount")
	tips_waiting_amount += _amount
	_context = _tip.get("context")
	_channel = _context.get_info("channel")
	if _channel[0] == "#":
		_message.append("\002You tipped me %i DOGE on %s [hash: \00304%s\003]..." % (_amount, _channel, hash))
		_message.append("\002> Say rain <hash> to make them rain anonymously on %s" % _channel)
	else:
		_message.append("\002You tipped me %i DOGE in private [hash: \00304%s\003]..." % (_amount, hash))
	_message.append("\002> Type +rain <hash> where you want to make them rain.")
	_message.append("\002> Or say return <hash> to get them back.")
	_message.append("\002> Else, I will keep them in %i minutes." % int(tip_timeout/60))
	_source = _tip.get("source")
	for _message_part in _message:
		_context.command("msg %s %s" % (_source, _message_part))
#
def tip_manage_auth(user, context, msg):
	args = (msg.strip()).split(' ')
	_cmd = args[0]
	_args = args[1:]
	_channel = context.get_info("channel")
	print("Tip management asked by '%s' on '%s' with cmd '%s' and args '%s'" % (user, _channel, _cmd, _args))
	if len(_args) != 1:
		context.command("msg %s Sorry, %s, not enough arguments for command '%s', use '%s <hash>'." % (user, user, _cmd, _cmd))
	else:
		print("Checking the management rights...")
		if (_args[0].lower() in tips):
			_tip_hash = _args[0].lower()
			_tip = tips.get(_tip_hash)
			print("Tip [%s] found. Checking the name..." % _tip_hash)
			_source = _tip.get("source")
			# _account = _tip.get("account")
			if (_source.lower() == user.lower()):
				print("Tip [%s] confirmed for user %s. Proceeding the action..." % (_tip_hash, user))
				tip_manage(user, context, _cmd, _tip_hash, "user request")
			else:
				print("User %s has no management rights on tip [%s]." % (user, _tip_hash))
				context.command("msg %s Sorry, %s, this tip belongs to nickname %s. If that is registred to you, recover the nickname or the account and try again." % (user, user, _source))
		else:
			print("Tip [%s] not found." % _args[0])
			context.command("msg %s Sorry, %s, I have no tip with hash [%s] in my list." % (user, user, _args[0]))
#
def tip_manage(user, context, cmd, hash, reason):
	global tips
	global tips_waiting_amount
	print("Processing action %s on tip [%s] for user %s" % (cmd, hash, user))
	_tip = tips.get(hash)
	_tip_amount = _tip.get("amount")
	if (cmd.lower() == "keep"):
		if hash in tips:
			print("Preparing to keep tip [%s]" % (hash))
			context.command("me will keep the tip [%s]. Thanks, %s. This will be tipped randomly among shibes." % (hash, user))
			print("Reducing tip amount (%s) from tips_waiting_amount" % (_tip_amount))
			tips_waiting_amount -= _tip_amount
			print("Deleting tip [%s]. Reason: Timeout." % hash)
			del tips[hash]
			print("Done")
		else:
			context.command("me Sorry, %s, I find no tip with hash [%s]." % (user, hash))
	if (cmd.lower() == "return"):
		print("Preparing to return tip [%s] to user %s. Getting correct context for return..." % (hash, user))
		_context = _tip.get("context")
		print("Returning tip [%s] to user %s." % (hash, user))
		_context.command("msg Doger tip %s %i" % (user, _tip_amount))
		print("Reducing the tips_waiting_amount")
		tips_waiting_amount -= _tip_amount
		print("Deleting tip from tips...")
		del tips[hash]
		print("Done.")
		if _context.get_info("channel")[0] == '#':
			_context.command("me returned tip [%s] to user %s as requested. Given reason: %s." % (hash, user, reason))
		else:
			if context.get_info("channel")[0] == '#':
				context.command("me returned tip [%s] to user %s as requested. Given reason: %s." % (hash, user, reason))
			else:
				_context.command("msg %s I returned you the tip [%s] as requested. Given reason: %s." % (user, hash, reason))
	if (cmd.lower() == "rain"):
		print("Preparing to rain tip [%s] as requested by user %s. Checking the context..." % (hash, user))
		_channel = context.get_info("channel")
		if (_channel[0] == "#"):
			print("Context found as channel '%s'" % _channel)
			print("Tip [%s] will be rained on '%s' as from user '%s'." % (hash, _channel, user))
			# such public rain
			rain_(hash, context, user, 0)
		else:
			print("Context found: private message. Checking original tip context...")
			_context = _tip.get("context")
			print("Checking if original context is a channel...")
			_channel = _context.get_info("channel")
			if (_channel[0] == "#"):
				print("Original context found to be channel '%s'." % _channel)
				print("Tip [%s] will be rained on '%s' as anonymous." % (hash, _channel))
				# such anonymous rain
				rain_(hash, _context, user, 1)
			else:
				print("Original context found to be private message. Can't rain in private message. ERROR")
				_context.command("msg %s Sorry, %s, as you tipped [%s] in private message, you have to use +rain <hash> on the channel you want your rain to come" % (user, user, hash))
#
def rain_(hash, context, user, anonymous):
	global tips_waiting_amount
	print("Preparing to rain tip [%s]..." % hash)
	_tip = tips.get(hash)
	_tip_amount = _tip.get("amount")
	_tip_bot = _tip.get("bot")
	print("Getting user count...")
	_users = get_rain_users(context)
	if (_users == None):
		# No users to rain, return the tip.
		tip_manage(user, context, "return", hash, "no users to rain - overwhelming error occured - behave!")
	else:
		_nicks = [((_users.get(_user)).get("nick")) for _user in _users]
		_weight = len(_nicks)
		rain_params = data.get("rain_params")
		_tip_min = (rain_params.get("bots")).get(_tip_bot).get("min")
		if (_tip_amount < (_tip_min * _weight)):
			print("Not enough to rain (raining %i on %i users) [_tip_min: %i]. Returning the tip..." % (_tip_amount, _weight, _tip_min))
			tip_manage(user, context, "return", hash, "not enough to rain (%i DOGE on %i users, minimum tip: %i DOGE/user * %i users = %i DOGE)" % (_tip_amount, _weight, _tip_min, _weight, (_tip_min * _weight)))
		else:
			_drop_weight = int(_tip_amount/_weight)
			print("There is enough (%i DOGE > %i DOGE = %i DOGE/user * %i users) to rain. Raining %i DOGE/user..." % (_tip_amount, (_tip_min * _weight), _tip_min, _weight, _drop_weight))
			_pack = [("%s %s" % (_nick, _drop_weight)) for _nick in _nicks]
			context.command("msg %s mtip %s" % (_tip_bot, ' '.join(_pack)))
			print("Reducing the tips_waiting_amount")
			tips_waiting_amount -= _tip_amount
			print("Deleting the tip from tips...")
			del tips[hash]
			print("Done.")
			print("Checking anonymity...")
			if (anonymous == 1):
				print(" wow. such anonymous. so rain")
				_maker = "Anonymous shibe"
			else:
				print(" wow. such public. so rain")
				_maker = user
			print("Raining...")
			current_context_command_msg_chan(context, "%s rained %i DOGE on: %s" % (_maker, _drop_weight, ', '.join(_nicks)))
#
def get_rain_users(context):
	rain_params = data.get("rain_params")
	print("Preparing to get rain list...")
	_rain_users = {}
	print("Getting context users...")
	_context_users = context.get_list("users")
	print("Checking user list...")
	for _user in _context_users:
		if _user.account in _rain_users:
			print("Clone detected for account %s: nick %s." % (_user.account, _user.nick))
		else:
			print("New account detected: %s. Checking ban list." % _user.account)
			rain_ban = rain_params.get("rain_ban")
			if _user.account.lower() in rain_ban:
				print("Account %s found in ban list, checking nicknames." % _user.account)
				_user_ban = rain_ban.get(_user.account.lower())
				if not (( _user.nick.lower() in _user_ban.get("nicks")) or ("all" in _user_ban.get("nicks"))):
					_rain_users.update({_user.account: {"nick": _user.nick, "lasttalk": _user.lasttalk}})
			else:
				print("Account '%s' will be added with nickname '%s'" % (_user.account, _user.nick))
				_rain_users.update({_user.account: {"nick": _user.nick, "lasttalk": _user.lasttalk}})
	_rain_drops = len(_rain_users)
	if (_rain_drops == 0):
		print("No users found. WTF!")
		return None
	else:
		rain_timeout = rain_params.get("rain_timeout")
		print("Checking user activity... [_rain_drops: %i | rain_timeout: %i]" % (_rain_drops, rain_timeout))
		_rain_users_tmp = _rain_users.copy()
		for _user_name in _rain_users:
			_user = _rain_users.get(_user_name)
			_user_lasttalk = _user.get("lasttalk")
			if ((time.time() - _user_lasttalk) > rain_timeout):
				print("User with nick %s (last active: %i) timed out by %i seconds. Deleting from the list..." % (_user.get("nick"), _user_lasttalk, (time.time() - _user_lasttalk - rain_timeout)))
				del _rain_users_tmp[_user_name]
		_rain_users = _rain_users_tmp
		_rain_drops_new = len(_rain_users)
		print("Activity check deleted %i users." % (_rain_drops - _rain_drops_new))
		if _rain_drops_new == 0:
			print("No users found. All were deleted. WTF! (consider ERROR)")
			return None
		else:
			return _rain_users
#
def get_account_(nick, context):
	if nick == "":
		print("ERROR in nickname from get_account_")
		return ""
	else:
		_users = context.get_list("users")
		found = 0
		for _user in _users:
			if (_user.nick.lower() == nick.lower()):
				found = 1
				return _user.account
		if found != 1:
			return ""
#
def api_coldcryptos(_get, _coin_0, _coin_1):
	# Getting information
	if (_get in ["info", "list"]):
		req = requests.get("http://www.coldcryptos.com/api/coins_info")
		if (req.status_code != 200):
			return req.status_code
		else:
			req_dict = req.json()
			if req_dict.get("message") != "OK":
				return -1
			else:
				req_data = req_dict.get("data")
				if (_get == "list"):
					return req_data.keys()
				else:
					# getting "info"
					if (_coin_0.upper() in req_data):
						_coin = req_data.get(_coin_0.upper())
						_msg = "Name: %(coin_name)s\nBlock time: %(block_time)s\nWallet version: %(wallet_version)s | last update: %(wallet_last_update)s\nNetwork fee: %(network_withdraw_fee)s" % _coin
						return _msg
					else:
						return ("ERROR: coin %s not found." % _coin_0)
	else:
		# _get == "ticker"
		req = requests.get("http://www.coldcryptos.com/api/ticker")
		if (req.status_code != 200):
			return ("ERROR: %s." % req.status_code)
		else:
			req_dict = req.json()
			if req_dict.get("message") != "OK":
				return ("ERROR: %s." % req_dict.get("message"))
			else:
				req_data = req_dict.get("data")
				_pair = ("%s/%s" % (_coin_0, _coin_1)).upper()
				print(_pair)
				if _pair in req_data:
					_coin = req_data.get(_pair)
					_msg = ("%(pair_name)s: \002\00302,00ColdCryptos\003\002 [high: %(high)s | low: %(low)s]") % _coin
					return _msg
				else:
					return ("ERROR: pair %s not found." % _pair)
#
def api_bittrex(coin_0, coin_1):
	try:
		_exchange = "%(bold)sBIT%(bold)strex     " % hexchat_format
		req = requests.get("https://bittrex.com/api/v1.1/public/getticker?market=%s-%s" % (coin_1.upper(), coin_0.upper()))
		if (req.status_code != 200):
			return {"success": False, "error": ("Error %s from BITtrex" % req.status_code)}
		else:
			if (req.json().get("success") == True):
				_last = req.json().get("result").get("Last")
				_sell = req.json().get("result").get("Ask")
				_buy = req.json().get("result").get("Bid")
				return {"success": True, "result": {"last": _last, "sell": _sell, "buy": _buy}, "exchange": _exchange}
			else:
				return {"success": False, "error": req.json().get("message")}
	except:
		return {"success": False, "error": "Error from api_bittrex()"}
#
def api_bter(coin_0, coin_1):
	try:
		_exchange = "%(colour)s04B%(colour)s07ter%(colour)s        " % hexchat_format
		req = requests.get("http://data.bter.com/api/1/ticker/%s_%s" % (coin_0.lower(), coin_1.lower()))
		if (req.status_code != 200):
			return {"success": False, "error": ("Error %s from Bter" % req.status_code)}
		else:
			req_dict = req.json()
			_last = float(req_dict.get("last"))
			_sell = float(req_dict.get("sell"))
			_buy = float(req_dict.get("buy"))
			return {"success": True, "result": {"last":_last, "sell":_sell, "buy":_buy}, "exchange": _exchange}
	except:
		return {"success": False, "error": "Error from api_bter()"}
#
def api_mintpal(coin_0, coin_1):
	try:
		_exchange = "%(colour)s03mintpal%(colour)s     " % hexchat_format
		req = requests.get("https://api.mintpal.com/v1/market/stats/%s/%s" % (coin_0, coin_1))
		if (req.status_code != 200):
			return {"success": False, "error": ("Error %s from Mintpal" % req.status_code)}
		else:	
			req_dict = req.json()[0]
			_last = float(req_dict.get("last_price"))
			_sell = float(req_dict.get("top_ask"))
			_buy = float(req_dict.get("top_bid"))
			_change = float(req_dict.get("change"))
			return {"success": True, "result": {"last": _last, "sell": _sell, "buy": _buy, "change": _change}, "exchange": _exchange}
	except:
		return {"success": False, "error": "Error from api_mintpal()"}
#
def api_cryptonator(coin_0, coin_1):
	try:
		_exchange = "%(colour)s00,02Cryptonator%(colour)s " % hexchat_format
		req = requests.get("https://www.cryptonator.com/api/ticker/%s-%s" % (coin_0, coin_1))
		if (req.status_code != 200):
			return {"success": False, "error": ("Error %s from Cryptonator" % req.status_code)}
		else:
			req_dict = req.json()
			if (req_dict.get("success") != True):
				return {"success": False, "error": ("Error from Cryptonator: %s" % req_dict.get("error"))}
			else:
				_last = float(req_dict.get("ticker").get("price"))
				_sell = _last
				_buy = _last
				return {"success": True, "result": {"last": _last, "sell": _sell, "buy": _buy}, "exchange": _exchange, "pair": [req_dict.get("ticker").get("base"), req_dict.get("ticker").get("target")]}
	except:
		return {"success": False, "error": "Error from api_cryptonator()"}
#
def api_bleutrade(coin_0, coin_1):
	try:
		_exchange = "%(colour)s00,06 Bleutrade %(colour)s " % hexchat_format
		req = requests.get("https://bleutrade.com/api/v2/public/getticker?market=%s_%s" % (coin_0.upper(), coin_1.upper()))
		if (req.status_code != 200):
			return {"success": False, "error": ("Error %s from Bleutrade" % req.status_code)}
		else:
			req_dict = req.json()
			if (req_dict.get("success") != "true"):
				return {"success": False, "error": ("Error from Bleutrade: %s" % req_dict.get("message"))}
			else:
				_last = float(req_dict.get("result")[0].get("Last"))
				_sell = float(req_dict.get("result")[0].get("Ask"))
				_buy = float(req_dict.get("result")[0].get("Bid"))
				return {"success": True, "result": {"last": _last, "sell": _sell, "buy": _buy}, "exchange": _exchange, "pair": [coin_0.upper(), coin_1.upper()]}
	except:
		return {"success": False, "error": "Error from api_bleutrade()"}
#
def api_ticker_custom(coin_0, coin_1):
	_exchange = "%(bold)smyTICKER%(bold)s    " % hexchat_format
	_pair = "%s_%s" % (coin_0.lower(), coin_1.lower())
	tickers_custom = data.get("ticker_custom")
	if _pair in tickers_custom:
		_pair_tickers = data.get("ticker_custom").get(_pair)
		_last = _pair_tickers.get("last")
		if "buy" in _pair_tickers:
			_buy = _pair_tickers.get("buy")
		else:
			_buy = _last
		if "sell" in _pair_tickers:
			_sell = _pair_tickers.get("sell")
		else:
			_sell = _last
		return {"success": True, "result": {"last": _last, "sell": _sell, "buy": _buy}, "exchange": _exchange, "pair": [coin_0.upper(), coin_1.upper()]}
	else:
		return {"success": False, "error": ("Error from data.get(\"ticker_custom\"): %s" % "Pair not found.")}
#
def api_ticker(user, context, cmd, args):
	if len(args) != 1:
		context.command("msg %s ERROR: not enough or too many arguments for 'ticker'." % context.get_info("channel"))
	else:
		_last = 0
		_sell = 0 # ask
		_buy = 0 # bid
		_change = 0 # %+.2f%%
		# Getting ticker
		tickers = []
		try:
			tickers.append(api_ticker_custom(args[0], "btc"))
		except:
			print("Error from api_ticker() while trying to add: Ticker_Custom")
		try:
			tickers.append(api_bter(args[0], "btc"))
		except:
			print("Error from api_ticker() while trying to add: Bter")
		try:
			tickers.append(api_bittrex(args[0], "btc"))
		except:
			print("Error from api_ticker() while trying to add: BITtrex")
		try:
			tickers.append(api_bleutrade(args[0], "btc"))
		except:
			print("Error from api_ticker() while trying to add: Bleutrade")
		#try:
		#	tickers.append(api_mintpal(args[0], "btc"))
		#except:
		#	print("Error from api_ticker() while trying to add: Mintpal")
		#try:
		#	tickers.append(api_cryptonator(args[0], "btc"))
		#except:
		#	print("Error from api_ticker() while trying to add: Cryptonator")
		# Getting info from ticker
		for ticker in tickers:
			if ticker.get("success") != True:
				print(ticker.get("error"))
			else:
				_message = ""
				_last = ticker.get("result").get("last")
				_sell = ticker.get("result").get("sell")
				_buy = ticker.get("result").get("buy")
				if (_last < 0.0001) or (_sell < 0.0001) or (_buy < 0.0001):
					_unit = "SAT"
					_last = "%i" % int(_last * 1e+8)
					_sell = "%i" % int(_sell * 1e+8)
					_buy = "%i" % int(_buy * 1e+8)
				else:
					_unit = "BTC"
					_last = "%.4f" % _last
					_sell = "%.4f" % _sell
					_buy = "%.4f" % _buy
				_message = "%s/%s: %s [\00313,00last: \002%s\002 %s\003 | \00304,00sell: \002%s\002 %s\003 | \00302,00buy: \002%s\002 %s\003]" % (args[0].upper(), "BTC", ticker.get("exchange"), _last, _unit, _sell, _unit, _buy, _unit)
				if "change" in ticker.get("result"):
					_message = "%s %+0.2f%%" % (_message, ticker.get("result").get("change"))
				current_context_command_msg_chan(context, "%s" % (_message))
#
def api_convert_coin(user, context, cmd, args):
	if (len(args) > 3 or len(args) < 2):
		current_context_command_msg_chan(context, "ERROR: Not enough or too many arguments for '%s'." % (cmd))
	else:
		value = 1.
		sources = []
		if (len(args) == 3):
			#try:
			value = float(args[0])
			print("value = %.8f" % value)
			#except:
			#	print("Error from api_convert_coin() while trying to get the value of args[0] (args[0]==%s)" % args[0])
		try:
			if len(args) == 3:
				sources.append(api_cryptonator(args[1], args[2]))
			else:
				# len(args) == 2
				sources.append(api_cryptonator(args[0], args[1]))
		except:
			print("Error from api_convert_coin() while trying to add: Cryptonator")
		try:
			if len(args) == 3:
				sources.append(api_ticker_custom(args[1], args[2]))
			else:
				# len(args) == 2
				sources.append(api_ticker_custom(args[0], args[1]))
		except:
			print("Error from api_convert_coin() while trying to add: Ticker_Custom")
		# Getting info from source
		for source in sources:
			if source.get("success") != True:
				print(source.get("error"))
			else:
				_message = ""
				_price = float(source.get("result").get("last"))*value
				if len(args) == 3:
					_unit_source = args[1].upper()
					if (_unit_source.lower() in ["btc", "ltc"]) and (value < 0.0001):
						value = "%i" % int(value * 1e+8)
						_unit_source = "%s %s" % (value, units.get(_unit_source.lower()).get("submultiple"))
					else:
						if value < 0.0001:
							_unit_source = "%.8f %s" % (value, args[1].upper())
						else:
							_unit_source = "%.4f %s" % (value, args[1].upper())
					_unit_target = args[2].upper()
				else:
					_unit_source = args[0].upper()
					_unit_target = args[1].upper()
				if _unit_target.lower() in ["btc", "ltc"] and (_price < 0.0001):
					_unit_target = units.get(_unit_target.lower()).get("submultiple")
					_price = "%i" % int(_price * 1e+8)
				else:
					_price = "%.4f" % _price
				_message = "%s: %s [\00313\002%s\002 %s\003]" % (_unit_source, source.get("exchange"), _price, _unit_target)
				current_context_command_msg_chan(context, _message)
#
def api_chucknorrisfact(user, context, cmd, args):
	args_TRI = ["last", "first", "top", "flop", "mtop", "mflop", "alea"]
	args_TYPE = ["txt", "img"]
	TRI = "alea"
	TYPE = "txt"
	ERROR = False
	if len(args) != 0:
		if (len(args) > 2):
			current_context_command_msg_chan(context, "Too many arguments for command '%s'" % (cmd))
			ERROR = True
		elif (len(args) == 1):
			if (args[0].lower() in args_TRI):
				# args[0] is a TRI
				TRI = args[0].lower()
			elif (args[0].lower() in args_TYPE):
				# args[0] is a TYPE
				TYPE = args[0].lower()
			else:
				current_context_command_msg_chan(context, "Bad argument: %s" % (args[0]))
				ERROR = True
		else:
			args_bad = []
			for arg in args:
				if ((arg.lower() not in args_TRI) and (arg.lower() not in args_TYPE)):
					args_bad.append(arg)
			if (len(args_bad) != 0):
				current_context_command_msg_chan(context, "Bad arguments: %s" % (' '.join(args_bad)))
				ERROR = True
			else:
				if (args[0].lower() in args_TRI) and (args[1].lower() in args_TYPE):
					TRI = args[0].lower()
					TYPE = args[1].lower()
				elif (args[0].lower() in args_TYPE) and (args[1].lower() in args_TRI):
					TYPE = args[0].lower()
					TRI = args[1].lower()
				else:
					# Arguments are from the same set
					current_context_command_msg_chan(context, "ERROR on '%s': Arguments are from the same type." % (cmd))
					ERROR = True
	if not ERROR:
		req = requests.get("http://www.chucknorrisfacts.fr/api/get?data=tri:%s;type:%s;nb:1;page:1" % (TRI, TYPE))
		if (req.status_code != 200):
			hexchat.command("MSG %s ERROR: The server answered with error '%s'" % (context.get_info("channel"), req.status_code))
		else:
			req_json = req.json()[0]
			FACT_dict = {
				"id": req_json.get("id"), 
				"score": ((float(req_json.get("points"))/5)/float(req_json.get("vote")))*10, 
				"fact": HTMLParser.HTMLParser().unescape(req_json.get("fact"))
			}
			FACT_txt = ("#%(id)s [%(score).2f/10] %(fact)s" % FACT_dict)
			if PYTHON == 2:
				current_context_command_msg_chan(context, ("Chuck Norris fact for %s: %s" % (user, FACT_txt)).encode("UTF-8"))
			else:
				current_context_command_msg_chan(context, "Chuck Norris fact for %s: %s" % (user, FACT_txt))
#
def api_bitly(user, context, cmd, args):
	if is_auth(user, context, "owner"):
		bitly_params = data.get("bitly_params_owner")
	else:
		bitly_params = data.get("bitly_params")
	bitly_username = bitly_params.get("bitly_username")
	bitly_apikey = bitly_params.get("bitly_apikey")
	if len(args) != 1:
		current_context_command_msg_chan(context, "ERROR: Not enough or too many arguments for command '%s'." % (cmd))
	else:
		longURL = urllib_parse.quote_plus(args[0])
		print("api_bitly: longURL to shorten: %s" % longURL)
		bitly_api = "https://api-ssl.bitly.com/v3/shorten?login=%s&apiKey=%s&longUrl=%s&format=%s"
		req = requests.get(bitly_api % (bitly_username, bitly_apikey, longURL, "json"))
		if req.status_code != 200:
			current_context_command_msg_chan(context, "ERROR: Sorry, %s, Bitly answered with error #%s" % (user, req.status_code))
		else:
			req_json = req.json()
			if req_json.get("status_code") != 200:
				current_context_command_msg_chan(context, "ERROR: Sorry, %s, Bitly understood the request but answered with error #%s: '%s'" % (user, req_json.get("status_code"), req_json.get("status_txt")))
			else:
				req_data = req_json.get("data")
				context.command("ME \017shortened a link from \00307Bitly\003 for %s: \00302%s\003" % (user, req_data.get("url")))
#
def current_context_command_msg_chan(context, msg):
	context.command("msg %s %s" % (context.get_info("channel"), msg))
	# Telegram bridge
	if (context.get_info("channel").lower() in data.get("telegram_params").get("channels")) and not telegram_bifrost_enabled:
		telegram_bot_send_message(data.get("telegram_params").get("channels").get(context.get_info("channel").lower()), hexchat.strip(msg, -1, 3))
#
def current_context_command_msg_user(context, user, msg):
	context.command("msg %s %s" % (user.first_name, msg))
	# Telegram bridge (message user)
	if user.id != -1:
		print("sending message to user %s" % user.id)
		telegram_bot_send_message(user.id, hexchat.strip(msg, -1, 3))
#
def triggers_manager(trig, user, current_context, msg_full, words):
	triggers = data.get("triggers")
	if (trig == triggers.get("admins")) and (user.first_name.lower() in auth_users.get("admins")):
		cmd_admins(user.first_name, current_context, msg_full, words)
	if (trig == triggers.get("users")):
		cmd_users(user.first_name, current_context, msg_full, words)
	if (trig == triggers.get("api")):
		cmd_api(user.first_name, current_context, words[0], words[1:])
	if (trig == triggers.get("susers_sp")) and (user.first_name.lower() in auth_users.get("users_sp")):
		cmd_users_sp(user.first_name, current_context, words[0], words[1:])
	if (trig == triggers.get("help")) and (words[0].lower() == "help"):
		get_help(user, current_context, words[0], words[1:])
#
def get_irc_channel_users(user, chat, original_message_id):
	if chat.id in telegram_group_for_irc:
		current_context = hexchat.find_context(channel = telegram_group_for_irc.get(chat.id))
		cc_users = current_context.get_list("users")
		cc_users_nicks_pack = [("-- %s" % (i.nick)) for i in cc_users]
		if len(cc_users_nicks_pack) == 0:
			telegram_bot_send_message(user.id, "The channel is... void?!")
		else:
			telegram_bot_send_message(user.id, "List of users on channel %s as you requested:\n%s." % (current_context.get_info("channel"), " ;\n".join(cc_users_nicks_pack)))
	else:
		telegram_bot_send_message(chat.id, "Sorry %s, you are not on a bridged group." % user.first_name, original_message_id)
#
#--------------------------------------------------------------
# Auto-functions
#--------------------------------------------------------------
# Checks the balance at reload (or load if already connected with NickServ)
if not LOCAL:
	check_bal(__module_name__, None, "checkbal", [])
#
