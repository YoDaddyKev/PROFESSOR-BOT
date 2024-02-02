class script(object):  
    START_TXT = """🔮<i>>{user}.</i>🔮

<i>I'm {bot}.</i>

<i>Listen up, weakling. I've got a collection of movies that'll send shivers down your spine. Join our group, and maybe, just maybe, you'll survive the cinematic chaos we're about to unleash. Consider yourself warned.</i>"""
    
    HELP_TXT = "<i> {} Get Help Below, Suit Yourself </i>"

    ABOUT_TXT = """🔮 <b><i>MyNAME: {}</b></i>
🔮 <b><i>DEVELOPER: <a herf=https://t.me/k_ASTRA1>ReDIRECT</a></b></i>
🔮 <b><i>CODED ON: PyTHON / PyROGRAM</b></i>
🔮 <b><i>MyDATABASE: MONGO_DB</b></i>
🔮 <b><i>MySERVER: AnyWHERE</b></i>
🔮 <b><i>VERSION: V1.0</b></i>"""
   
    SOURCE_TXT = """<b><i>Source Code:</b></i>
<b><i>Limited ownership of components. Not available for public release.</b></i>

<b><i>For Enquires: @k_ASTRA1</b></i>"""

    FILE_TXT = """<b><i>File Store</b></i>

<b><i>Utilize this module to store files in my database, and receive a permanent link for access. For files from public channels, send the file link only. For private channels, grant admin access to enable file addition.</b></i>

<b><i>Command & Usage</b></i>
<code>/link</code> <b><i>Reply To Any Media To Get The Link </b></i>
<code>/batch</code> <b><i>To Create Link For Multiple Media</b></i>

<b><i>EG:</b></i>
</code>/batch https://t.me/k_ASTRA1/1 https://t.me/k_ASTRA1/10</code>"""
  
    FILTER_TXT = "<b><i>Select Which One You Want...</b></i>"
    
    GLOBALFILTER_TXT = """<b><i>Help For Global Filters</b></i>

<b><i>Filter Is The Feature Were Users Can Set Automated Replies For A Particular Keyword And Bot  Will Respond Whenever A Keyword Is Found The Message</b></i>

<b><i>Note:</b></i>
<b><i>This Module Only Works For My Admins</b></i>

<b><i>Commands And Usage:</b></i>
🔮 <code>/gfilter</code> - <b><i>To Add Global Filters</b></i>
🔮 <code>/gfilters</code> - <b><i>To View List Of All Global Filters</b></i>
🔮 <code>/delg</code> - <b><i>To Delete A Specific Global Filter</b></i>
🔮 <code>/delallg</code> - <b><i>To Delete All Global Filterꜱ</b></i>

🔮 <code>/g_filter</code> <b><i>off Use This Command + on/off In Your Group To Control Global Filter In Your Group</b></i>"""

    MANUELFILTER_TXT = """🔮<b><i>Help: Filters</b></i>🔮

<b><i>Filter Is The Feature Were Users Can Set Automated Replies For A Particular Keyword And Bot  Will Respond Whenever A Keyword Is Found The Message</b></i>

<b><i>Note:</b></i>
<b><i>1. This Bot Should Have Admin Privillage.</b></i>
<b><i>2. Only Admins Can Add Filters In A Chat.</b></i>
<b><i>3. Alert Buttons Have A Limit Of 64 Characters.</b></i>

<b>Commands And Usage:</b>
🔮 <code>/filter</code> - <b><i>Add A Filter In Chat</b></i>
🔮 <code>/filters</code> - <b><i>List All The Filters Of A Chat</b></i>
🔮 <code>/del</code> - <b><i>Delete A Specific Filter In Chat</b></i>
🔮 <code>/delall</code> - <b><i>Delete The Whole Filters In A Chat (Chat Owner Only)</b></i>

- <code>/g_filter</code> <b><i>Use This Command + on/off In Your Group To Control Global Filter In Your Group</b></i>"""

    BUTTON_TXT = """🔮<b><i>Help: Buttons</b></i>🔮

<b><i>This Bot Supports Both Url And Alert Inline Buttons.</b></i>

<b><i>Note:</b></i>
<b><i>1. Telegram Will Not Allows You To Send Buttons Without Any Content, So Content Is Mandatory.</b></i>
<b><i>2. This Bot Supports Buttons With Any Telegram Media Type.</b></i>
<b><i>3. Buttons Should Be Properly Parsed As Markdown Format</b></i>

<b><i>URL Buttons:</b></i>
<code>[Button Text](buttonurl:xxxxxxxxxxxx)</code>

<b><i>Alert Buttons:</b></i>
<code>[Button Text] (Button Alert: This Is An Alert Message)</code>"""

    AUTOFILTER_TXT = """🔮<b><i>Help For AutoFilter</b></i>🔮

<b><i>Auto Filter Is The Feature To Filter & Save The Files Automatically From Cuannel To Group. You Can Use The Following Command To on/off The AutoFilter In Your Group</b></i>

- <code>/autofilter on</code> - <b><i>autofilter enable in your chat</b></i>
- <code>/autofilter off</code> - <b><i>autofilter disabled in your chat</b></i>

<b><i>Other Commands:</b></i>
🔮 <code>/set_template</code> - <b><i>Set Imdb Template For Your Group</b></i> 
🔮 <code>/get_template</code> - <b><i>Get Current Imdb Template For Your Group</b></i>"""

    CONNECTION_TXT = """🔮<b><i>Help For Connections</b></i>🔮

<b><i>Used To Connect Bot To Pm For Managing Filters. It Helps To Avoid Spamming In Groups</b></i>

<b><i>NOTE:</b></i>
🔮 <b><i>Only Admins Can Add A Connection.</b></i>
🔮 <b><i>Send <code>/connect</code> <b><i>For Connecting Me To Your Pm</b></i>

<b><i>Commands And Usage:</b>
🔮 <code>/connect</code>  - Connect A Particular Chat To Your PM
🔮 <code>/disconnect</code>  - Disconnect From A Chat
🔮 <code>/connections</code>  - List All Your Connections"""

    ADMIN_TXT = """🔮<b><i>Help: Admins Only</b></i>🔮
    
<b><i>NOTE: This Module Only Works For Admins</b></i>

<b><i>Commands & Usage</b></i>
🔮 <code>/logs</code> - <b><i>To Get The Recent Errorꜱ</b></i>
🔮 <code>/delete</code> - <b><i>To Delete A Specific File From DB</b></i>
🔮 <code>/deleteall</code> - <b><i>To Delete All Files From DB</b></i>
🔮 <code>/users</code> - <b><i>To Get Liꜱt Of My Uꜱerꜱ And IDS</b></i>
🔮 <code>/chats</code> - <b><i>To Get Liꜱt Of My Chatꜱ And IDS</b></i>
🔮 <code>/channel</code> - <b><i>To Get Liꜱt Of Total Connected Channelꜱ</b></i>
🔮 <code>/broadcast</code> - <b><i>To Broadcaꜱt A Meꜱꜱage To All Uꜱerꜱ</b></i>
🔮 <code>/group_broadcast</code> - <b><i>To Broadcast A Message To All Connected Groups</b></i>
🔮 <code>/leave</code>  - <b><i>(With Chat’s ID) To Leave From A Chat</b></i>
🔮 <code>/disable</code>  - <b><i>(With Chat’s ID) To Diꜱable A Chat</b></i>
🔮 <code>/invite</code> - <b><i>(With Chat’s ID) To Get The Invite Link Of Any Chat Where The Bot Is Admin</b></i>
🔮 <code>/ban_user</code>  - <b><i>(With User’s ID) To Ban A Uꜱer</b></i>
🔮 <code>/unban_user</code>  - <b><i>(With User’s ID) To Unban A Uꜱer</b></i>
🔮 <code>/restart</code> - <b><i>To Restart The Bot</b></i>
🔮 <code>/clear_junk</code> - <b><i>Clear All Delete Account & Blocked Account In Database</b></i>
🔮 <code>/clear_junk_group</code> - <b><i>Clear Add Removed Group Or Deactivated Groups On DB</b></i>"""


    STATUS_TXT = """🔮 Total Files: <code>{}</code>
🔮 <b><i>Total Users:</b></i> <code>{}</code>  
🔮 <b><i>Total Chats:</b></i> <code>{}</code>
🔮 <b><i>Capacity Of Used Space (DB):</b></i> <code>{}</code>
🔮 <b><i>Space Remaining:</b></i> <code>{}</code>"""

    LOG_TEXT_G = """New Group!

🔮 <b><i>Group:</b></i> {a}
🔮 <b><i>ID (Group):</b></i> <code>{b}</code>
🔮 <b><i>Link (Group):</b></i> @{c}
🔮 <b><i>Members Count (Group):</b></i> <code>{d}</code>
🔮 <b><i>Added BY:</b></i> {e}

🔮 <b><i>BY</b></i>: @{f}"""
  
    LOG_TEXT_P = """New User!
    
🔮 <b><i>User Id:</b></i> <code>{}</code>
🔮 <b><i>User’s Name:</b></i> {}
🔮 <b><i>UserName:</b></i> @{}

🔮 <b><i>BY:</b></i> @{}"""
  
    GROUPMANAGER_TXT = """🔮<b><i>Help: Group Managing</b></i>🔮

<b><i>Thiꜱ Iꜱ Helps Your Group Managing. Thiꜱ Will Work Only For Group ADMINS!</b></i>

<b><i>Command & Uꜱage:</b></i>
🔮 <code>/inkick</code> - <b><i>Command With Required Arguments And I Will Kick Members From Group.</b></i>
🔮 <code>/instatus</code> - <b><i>To Check Current Status Of Chat Member From Group.</b></i>
🔮 <code>/dkick</code> - <b><i>To Kick Deleted Accounts</b></i>
🔮 <code>/ban</code> - <b><i>To Ban A Uꜱer Form The Group</b></i>
🔮 <code>/unban</code> - <b><i>Unban The Banned Uꜱer</b></i>
🔮 <code>/tban</code> - <b><i>Temporary Ban A Uꜱer</b></i>
🔮 <code>/mute</code> - <b><i>To Mute A Uꜱer</b></i>
🔮 <code>/unmute</code> - <b><i>To Unmute The Muted Uꜱer</b></i>
🔮 <code>/tmute</code> - <b><i>With Value To Mute Up To Particular Time EG:</b></i> <code>/tmute 2h</code> <b><i>To Mute 2 Hour Valueꜱ Iꜱ )m/h/d)</b></i>
🔮 <code>/pin</code> - <b><i>To Pin A Meꜱꜱage On Your Chat</b></i>
🔮 <code>/unpin</code> - <b><i>To Unpin The Meꜱꜱage On Your Chat</b></i>
🔮 <code>/purge</code> - <b><i>Delete All Messages From The Replied To Message, To The Current Message</b></i>"""

    EXTRAMOD_TXT = """🔮<b><i>Help: Extra Modules</b></i>🔮

<b><i>Send Any Image (To Edit)</b></i>

<b><i>Commands & Usage</b></i>
🔮 <code>/id</code> - <b><i>Get Id Of A Specifed User</b></i>
🔮 <code>/info</code>  - <b><i>Get Information About A User</b></i>
🔮 <code>/imdb</code>  - <b><i>Get The Film Information From Imdb Source</b></i>
🔮 <code>/paste [TEXT]</code> - <b><i>Paste The Given Text On Pasty</b></i>
🔮 <code>/tts [TEXT]</code> - <b><i>Convert Text To Speech</b></i>
🔮 <code>/telegraph</code> - <b><i>Send Me This Command Reply With Picture Or Vide Under (5mb)</b></i>
🔮 <code>/json</code> - <b><i>Reply With Any Meꜱꜱage To Get Meꜱꜱage Info) uꜱeful for group</b></i>
🔮 <code>/written</code> - <b><i>Reply With Text To Get File (uꜱeful for coderꜱ)</b></i>
🔮 <code>/carbon</code> - <b><i>Reply With Text To Get Carbonated Image</b></i>
🔮 <code>/font [TEXT]</code> - <b><i>To Change Your Text Fonts To Fancy Font</b></i>
🔮 <code>/share</code> - <b><i>Reply With Text To Get Text Sharable Link</b></i>
🔮 <code>/song [NAME]</code> - <b><i>To Search The Song In YouTube</b></i>
🔮 <code>/video [LINK]</code> - <b><i>To Download The YouTube Video</b></i>"""    
    
    CREATOR_REQUIRED = "❗<b>Yᴏᴜ Hᴀᴠᴇ To Bᴇ Tʜᴇ Gʀᴏᴜᴩ Cʀᴇᴀᴛᴏʀ Tᴏ Dᴏ Tʜᴀᴛ</b>"
      
    INPUT_REQUIRED = "❗ **Aʀɢᴜᴍᴇɴ Rqᴜɪʀᴇᴅ**"
      
    KICKED = "✔️ Sᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ Kɪᴄᴋᴇᴅ {} Mᴇᴍʙᴇʀꜱ Acᴄᴏʀᴅɪɴɢ To Tʜᴇ Aʀɢᴜᴍᴇɴᴛꜱ Prᴏᴠɪᴅᴇᴅ"
      
    START_KICK = "Rᴇᴍᴏᴠɪɴɢ Iɴᴀᴄᴛɪᴠᴇ Mᴇᴍʙᴇʀs Tʜɪs Mᴀʏ Tᴀᴋᴇ A Wʜɪʟᴇ"
      
    ADMIN_REQUIRED = "❗<b>Iᴀᴍ Nᴏᴛ Aᴅᴍɪɴ Iɴ Tʜɪꜱ Cʜᴀᴛ Sᴏ Pʟᴇᴀꜱᴇ Aᴅᴅ Mᴇ Aɢᴀɪɴ Wɪᴛʜ Aʟʟ Pᴅᴍɪɴ Pᴇʀᴍɪꜱꜱɪᴏɴ</b>"
      
    DKICK = "✔️ Kɪᴄᴋᴇᴅ {} Dᴇʟᴇᴛᴇᴅ Aᴄᴄᴏᴜɴᴛꜱ Sᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ"
      
    FETCHING_INFO = "<b>Wᴀɪᴛ I Wɪʟʟ Tᴀᴋᴇ Tʜᴇ Aʟʟ Iɴꜰᴏ</b>"
   
    SERVER_STATS = """Sᴇʀᴠᴇʀ Sᴛᴀᴛꜱ:
 
Uᴩᴛɪᴍᴇ: {}
CPU Uꜱᴀɢᴇ: {}%
RAM Uꜱᴀɢᴇ: {}%
Tᴏᴛᴀʟ Dɪꜱᴋ: {}
Uꜱᴇᴅ Dɪꜱᴋ: {} ({}%)
Fʀᴇᴇ Dɪꜱᴋ: {}"""
    
    BUTTON_LOCK_TEXT = "Buddy {query}\nThis Iꜱ Not For You. Search Your Self"
   
    FORCE_SUB_TEXT = "Sᴏʀʀʏ Bʀᴏ Yᴏᴜʀ Nᴏᴛ Jᴏɪɴᴇᴅ Mʏ Cʜᴀɴɴᴇʟ Sᴏ Pʟᴇᴀsᴇ Cʟɪᴄᴋ Jᴏɪɴ Bᴜᴛᴛᴏɴ Tᴏ Jᴏɪɴ Mʏ Cʜᴀɴɴᴇʟ Aɴᴅ Tʀʏ Aɢᴀɪɴ"
   
    WELCOM_TEXT = """Hᴇʏ {user} 💞

Wᴇʟᴄᴏᴍᴇ ᴛᴏ {chat}.

ꜱʜᴀʀᴇ & ꜱᴜᴩᴩᴏʀᴛ, ʀᴇqᴜᴇꜱᴛ ʏᴏᴜ ᴡᴀɴᴛᴇᴅ ᴍᴏᴠɪᴇꜱ"""
  
    IMDB_TEMPLATE = """<b>Qᴜᴇʀʏ: {query}</b>

🏷 Tɪᴛʟᴇ: <a href={url}>{title}</a>
🎭 Gᴇɴʀᴇꜱ: {genres}
📆 Yᴇᴀʀ: <a href={url}/releaseinfo>{year}</a>
🌟 Rᴀᴛɪɴɢ: <a href={url}/ratings>{rating}</a>/10"""
   
  
 


   
  
 


