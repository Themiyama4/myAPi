import json
from flask import Flask, request, jsonify

channels = {"StarSports1": "https://edge4-moblive.yuppcdn.net/trans1sd/smil:starsports1.smil/playlist.m3u8",
            "StarSports2": "Expired",
            "SonyTv1": "https://edge4-moblive.yuppcdn.net/trans1sd/smil:tensports1.smil/playlist.m3u8",
            "SonyTv2": "https://edge4-moblive.yuppcdn.net/trans1sd/smil:tensports2.smil/playlist.m3u8",
            "SonyTv5": "https://edge4-moblive.yuppcdn.net/trans1sd/smil:tensports5.smil/playlist.m3u8",
            "EventXtra": "https://edge4-moblive.yuppcdn.net/transsd/smil:eventtvextra.smil/playlist.m3u8",
            }
app = Flask(__name__)
@app.route('/Madu', methods=['GET'])
def index():
    ChName = request.args.get('ChName')
    for channel in channels:
        if ChName == channel :
                 return jsonify({ChName:channels[ChName]})
    return jsonify({ChName:"WrongName"})
#return json.dumps({'Channel': 'StarSports','url': ''})
if __name__ == '__main__':
    app.run(debug=True)
