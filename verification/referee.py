"""
CheckiOReferee is a base referee for checking you code.
    arguments:
        tests -- the dict contains tests in the specific structure.
            You can find an example in tests.py.
        cover_code -- is a wrapper for the user function and additional operations before give data
            in the user function. You can use some predefined codes from checkio.referee.cover_codes
        checker -- is replacement for the default checking of an user function result. If given, then
            instead simple "==" will be using the checker function which return tuple with result
            (false or true) and some additional info (some message).
            You can use some predefined codes from checkio.referee.checkers
        add_allowed_modules -- additional module which will be allowed for your task.
        add_close_builtins -- some closed builtin words, as example, if you want, you can close "eval"
        remove_allowed_modules -- close standard library modules, as example "math"

checkio.referee.checkers
    checkers.float_comparison -- Checking function fabric for check result with float numbers.
        Syntax: checkers.float_comparison(digits) -- where "digits" is a quantity of significant
            digits after coma.

checkio.referee.cover_codes
    cover_codes.unwrap_args -- Your "input" from test can be given as a list. if you want unwrap this
        before user function calling, then using this function. For example: if your test's input
        is [2, 2] and you use this cover_code, then user function will be called as checkio(2, 2)
    cover_codes.unwrap_kwargs -- the same as unwrap_kwargs, but unwrap dict.

"""

SENDGRID_COVER = '''
import sendgrid
import sendgrid.cio as cio
import json
cio.set_testing_mode()

try:
    from urllib.error import HTTPError
except ImportError:
    from urllib2 import HTTPError

class MockSpam(cio.MockSimple):
    def __init__(self, data):
        self.data = data

    def time_period_data(self, start_time, end_time):
        return filter(lambda a: end_time <= a['created'] <= start_time, self.data)

    def limit_data(self, limit, offset):
        return self.data[limit:limit + offset]

    def __call__(self, request):
        try:
            from urlparse import parse_qs
        except ImportError:
            from urllib.parse import parse_qs
        data = parse_qs(request.get_full_url().split('?')[1])

        start_time = end_time = limit = offset = None
        if 'start_time' in data:
            start_time = int(data['start_time'][0])

        if 'end_time' in data:
            end_time = int(data['end_time'][0])

        if 'limit' in data:
            limit = int(data['limit'][0])

        if 'offset' in data:
            offset = int(data['offset'][0])

        if start_time and end_time:
            data = self.time_period_data(start_time, end_time)
        else:
            data = self.limit_data(limit, offset)

        return sendgrid.Response(200, """Server: nginx
Date: Mon, 03 Apr 2017 14:43:27 GMT
Content-Type: text/plain; charset=utf-8
Content-Length: 0
Connection: close
X-Message-Id: wvYdP5GWR9aF5cneTovlHA
X-Frame-Options: DENY
Access-Control-Allow-Origin: https://sendgrid.api-docs.io
Access-Control-Allow-Methods: POST
Access-Control-Allow-Headers: Authorization, Content-Type, On-behalf-of, x-sg-elas-acl
Access-Control-Max-Age: 600
X-No-CORS-Reason: https://sendgrid.com/docs/Classroom/Basics/API/cors.html
""", json.dumps(list(data)))


def cover(func, in_data):
    mock = MockSpam([
        {"created":1399552400,"email":"hlficij@gmail.com","ip":"109.162.147.167"},
        {"created":1399543051,"email":"eiliied@hotmail.com","ip":"49.168.253.108"},
        {"created":1399540395,"email":"fkadcgb@hotmail.com","ip":"119.140.24.94"},
        {"created":1399535005,"email":"bhjfeia@mail.kz","ip":"12.14.10.23"},
        {"created":1399531821,"email":"bkdcbdl@gmail.com","ip":"99.5.232.70"},
        {"created":1399523783,"email":"icchabd@mail.kz","ip":"87.102.44.129"},
        {"created":1399514567,"email":"iegcfkb@gmail.com","ip":"31.74.40.32"},
        {"created":1399511915,"email":"bgagigd@aol.com","ip":"126.19.197.212"},
        {"created":1399511772,"email":"kibibkd@gmail.com","ip":"107.77.110.197"},
        {"created":1399509317,"email":"habgcjf@mail.com","ip":"156.14.149.252"},
        {"created":1399505854,"email":"ckjcjkd@aol.com","ip":"113.33.64.89"},
        {"created":1399496426,"email":"dbffflc@mail.com","ip":"180.141.202.163"},
        {"created":1399493148,"email":"llhggjl@aol.com","ip":"41.4.239.95"},
        {"created":1399488044,"email":"cddfadb@gmail.com","ip":"176.250.238.230"},
        {"created":1399479710,"email":"fgklgef@gmail.com","ip":"37.27.237.95"},
        {"created":1399469934,"email":"jledafl@aol.com","ip":"220.192.166.187"},
        {"created":1399468712,"email":"ijhffhg@yahoo.com","ip":"207.94.228.240"},
        {"created":1399467806,"email":"hfdcclg@gmail.com","ip":"60.169.212.175"},
        {"created":1399459594,"email":"jjdcalh@mail.com","ip":"124.168.199.161"},
        {"created":1399450994,"email":"kfljjdg@mail.kz","ip":"227.42.132.2"},
        {"created":1399444607,"email":"edejchf@hotmail.com","ip":"157.94.94.252"},
        {"created":1399442868,"email":"hhdaghg@mail.com","ip":"76.50.158.70"},
        {"created":1399441369,"email":"hcelgib@mail.kz","ip":"190.99.126.49"},
        {"created":1399432717,"email":"iikkegk@mail.kz","ip":"227.24.22.17"},
        {"created":1399432131,"email":"dlcibdd@gmail.com","ip":"71.22.248.190"},
        {"created":1399424867,"email":"eijkgja@mail.kz","ip":"197.143.82.17"},
        {"created":1399416376,"email":"jafhgec@gmail.com","ip":"51.68.244.244"},
        {"created":1399415251,"email":"kdlklgf@mail.com","ip":"6.61.148.36"},
        {"created":1399408926,"email":"cfgackc@mail.com","ip":"171.17.94.160"},
        {"created":1399406490,"email":"lcjejak@yahoo.com","ip":"143.254.58.28"},
        {"created":1399400304,"email":"jillegg@mail.com","ip":"18.253.63.56"},
        {"created":1399395128,"email":"acakicc@mail.kz","ip":"173.71.2.45"},
        {"created":1399390235,"email":"echbjki@mail.kz","ip":"146.158.25.55"},
        {"created":1399386553,"email":"ddakgca@mail.kz","ip":"219.61.231.103"},
        {"created":1399377356,"email":"keakcek@aol.com","ip":"63.227.105.51"},
        {"created":1399377289,"email":"ldalagi@mail.com","ip":"30.143.126.9"},
        {"created":1399367974,"email":"bkbglcc@gmail.com","ip":"17.38.216.209"},
        {"created":1399361525,"email":"eebakad@yahoo.com","ip":"44.244.49.172"},
        {"created":1399351902,"email":"flhddfc@hotmail.com","ip":"82.247.118.47"},
        {"created":1399346397,"email":"elfhefi@gmail.com","ip":"240.30.36.27"},
        {"created":1399338763,"email":"bgchfcj@aol.com","ip":"148.129.54.230"},
        {"created":1399330025,"email":"dfhhdje@hotmail.com","ip":"244.145.147.203"},
        {"created":1399324996,"email":"hebgiij@yahoo.com","ip":"193.200.71.63"},
        {"created":1399324843,"email":"ladjllh@aol.com","ip":"236.46.211.152"},
        {"created":1399323592,"email":"jjjbfel@yahoo.com","ip":"72.40.104.123"},
        {"created":1399320606,"email":"ibgchbe@hotmail.com","ip":"132.171.100.118"},
        {"created":1399312633,"email":"jdhcejg@mail.kz","ip":"177.102.191.24"},
        {"created":1399306308,"email":"gcbdiki@yahoo.com","ip":"173.111.159.0"},
        {"created":1399298899,"email":"dkkfdbi@aol.com","ip":"82.99.244.172"},
        {"created":1399293955,"email":"blfahdl@mail.com","ip":"64.61.48.71"},
        {"created":1399292609,"email":"hlcbccc@mail.kz","ip":"156.221.239.93"},
        {"created":1399283157,"email":"hdkfcge@mail.kz","ip":"241.234.36.49"},
        {"created":1399282059,"email":"ffdjgel@gmail.com","ip":"215.12.11.145"},
        {"created":1399272118,"email":"jhdhddh@hotmail.com","ip":"58.76.165.121"},
        {"created":1399263581,"email":"cbglddh@hotmail.com","ip":"60.47.115.245"},
        {"created":1399256975,"email":"galicei@mail.com","ip":"22.199.50.229"},
        {"created":1399249512,"email":"idcldfd@aol.com","ip":"203.196.30.191"},
        {"created":1399240335,"email":"jfkjcka@aol.com","ip":"224.237.70.25"},
        {"created":1399237022,"email":"fabdieh@aol.com","ip":"187.185.108.38"},
        {"created":1399234592,"email":"hjfbldh@hotmail.com","ip":"116.133.74.100"},
        {"created":1399226726,"email":"bihgagl@hotmail.com","ip":"127.179.82.60"},
        {"created":1399222376,"email":"igajgdb@mail.kz","ip":"179.145.98.72"},
        {"created":1399219790,"email":"ldgbjie@hotmail.com","ip":"84.238.57.215"},
        {"created":1399218009,"email":"kccgdci@mail.com","ip":"62.138.175.100"},
        {"created":1399217053,"email":"elfgikd@gmail.com","ip":"57.19.201.79"},
        {"created":1399210661,"email":"bbdclkd@yahoo.com","ip":"44.168.213.55"},
        {"created":1399203157,"email":"ceckgll@mail.kz","ip":"115.66.165.126"},
        {"created":1399193776,"email":"kefhhak@hotmail.com","ip":"186.4.167.55"},
        {"created":1399193682,"email":"cgieche@mail.kz","ip":"183.214.84.100"},
        {"created":1399187315,"email":"chieadg@hotmail.com","ip":"94.226.248.175"},
        {"created":1399178581,"email":"akjdlli@yahoo.com","ip":"43.38.39.8"},
        {"created":1399169651,"email":"eaffakl@yahoo.com","ip":"81.121.236.236"},
        {"created":1399160014,"email":"kjchdfi@aol.com","ip":"226.169.116.50"},
        {"created":1399157483,"email":"cbhjkec@mail.kz","ip":"146.219.231.34"},
        {"created":1399150775,"email":"hcjgake@hotmail.com","ip":"15.197.184.185"},
        {"created":1399144163,"email":"leabgia@aol.com","ip":"166.82.25.223"},
        {"created":1399142335,"email":"cfgeklk@mail.kz","ip":"196.180.119.211"},
        {"created":1399135258,"email":"gllhiik@mail.kz","ip":"210.99.191.23"},
        {"created":1399131244,"email":"kilbica@aol.com","ip":"167.78.224.186"},
        {"created":1399127203,"email":"bgbhfjc@hotmail.com","ip":"230.199.193.252"},
        {"created":1399117235,"email":"adbjbab@mail.com","ip":"22.111.50.235"},
        {"created":1399108024,"email":"ddldjdk@mail.com","ip":"32.27.4.32"},
        {"created":1399102061,"email":"ekjjhlg@hotmail.com","ip":"204.74.145.237"},
        {"created":1399093746,"email":"dgeagge@mail.kz","ip":"21.155.184.24"},
        {"created":1399084939,"email":"lkfjicb@aol.com","ip":"109.45.103.69"},
        {"created":1399081153,"email":"gfbcfic@yahoo.com","ip":"211.62.52.236"},
        {"created":1399077389,"email":"fklfahj@gmail.com","ip":"150.78.121.53"},
        {"created":1399076386,"email":"bfblkia@gmail.com","ip":"153.152.254.255"},
        {"created":1399071588,"email":"lbkadhk@gmail.com","ip":"227.95.245.237"},
        {"created":1399068509,"email":"eicgfjf@yahoo.com","ip":"141.255.167.67"},
        {"created":1399065934,"email":"ilacebg@hotmail.com","ip":"231.112.248.191"},
        {"created":1399065509,"email":"ckajblf@mail.kz","ip":"156.88.200.93"},
        {"created":1399063113,"email":"legijda@hotmail.com","ip":"195.34.214.7"},
        {"created":1399054775,"email":"kflbgdi@gmail.com","ip":"2.222.243.251"},
        {"created":1399053550,"email":"aagcalb@hotmail.com","ip":"215.109.142.90"},
        {"created":1399047732,"email":"bfifebf@mail.kz","ip":"153.146.169.56"},
        {"created":1399047553,"email":"gjjgkab@yahoo.com","ip":"49.55.100.161"},
        {"created":1399038183,"email":"bikehlj@mail.com","ip":"40.103.245.130"},
        {"created":1399033717,"email":"fafhkla@mail.com","ip":"54.253.109.218"},
        {"created":1399027409,"email":"bagieee@aol.com","ip":"137.46.80.103"}
    ])
    cio.set_mock('/suppression/spam_reports', mock)
    return func(*in_data)
    
'''

from checkio.signals import ON_CONNECT
from checkio import api
from checkio.referees.io import CheckiOReferee
from checkio.referees import cover_codes

from tests import TESTS

api.add_listener(
    ON_CONNECT,
    CheckiOReferee(
        tests=TESTS,
        function_name={
            "python": "how_spammed"
        },
        cover_code={
            'python-27': SENDGRID_COVER,
            'python-3': SENDGRID_COVER
        }
    ).on_ready)

