import requests
import json
import pandas as pd
import argparse
import time
import logging

logger = logging.getLogger(__name__)
file_handler = logging.FileHandler('log')
file_handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(message)s'))
logger.addHandler(file_handler)
logger.setLevel(logging.INFO)

class YoutubeCommentsExtractor:
    def __init__(self) -> None:
        self.__session = requests.Session()
        self.__innertubeApiKey = None
        self.__visitorData = None
        self.__initial_data = None
        self.__video_url = None
        self.__comments_df = None

    def extract(self, video_url: str, output_file: str):
        start_time = time.time()
        logger.info(f'Extracting from {video_url}')
        print(f'Extracting comments from {video_url}')
        self.__comments_df = pd.DataFrame()
        self.__video_url = video_url
        self.__initial_data = self.__get_initial_data()
        self.__get_comments(self.__initial_data)
        self.__comments_df.to_csv(output_file, index=False)
        print(f'{self.__comments_df.shape[0]} comments extracted and saved in {output_file}')
        total_time = time.time() - start_time
        logger.info(f'Extracted in {total_time} seconds.')

    def __get_initial_data(self) -> dict:
        header = {
            'Sec-Fetch-Site': 'none',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Host': 'www.youtube.com',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.2.1 Safari/605.1.15',
            'Connection': 'keep-alive',
            'Priority': 'u=0, i',
        }
        try:
            req = self.__session.get(self.__video_url, headers=header)
        except Exception as e:
            logger.setLevel(logging.ERROR)
            logger.error(e)
            raise Exception(f'Error while trying to access url {self.__video_url}.')

        if req.status_code != 200:
            raise Exception(
                f'Error when trying to access url, status: {req.status}')
        req_json = req.text.split('ytcfg.set(')
        req_json = req_json[2].split(');')[0]
        req_json = json.loads(req_json)
        hl = req_json['INNERTUBE_CONTEXT']['client']['hl']
        gl = req_json['INNERTUBE_CONTEXT']['client']['gl']
        remoteHost = req_json['INNERTUBE_CONTEXT']['client']['remoteHost']
        deviceMake = req_json['INNERTUBE_CONTEXT']['client']['deviceMake']
        deviceModel = req_json['INNERTUBE_CONTEXT']['client']['deviceModel']
        visitorData = req_json['INNERTUBE_CONTEXT']['client']['visitorData']
        userAgent = req_json['INNERTUBE_CONTEXT']['client']['userAgent']
        clientName = req_json['INNERTUBE_CONTEXT']['client']['clientName']
        clientVersion = req_json['INNERTUBE_CONTEXT']['client']['clientVersion']
        osName = req_json['INNERTUBE_CONTEXT']['client']['osName']
        osVersion = req_json['INNERTUBE_CONTEXT']['client']['osVersion']
        originalUrl = req_json['INNERTUBE_CONTEXT']['client']['originalUrl']
        platform = req_json['INNERTUBE_CONTEXT']['client']['platform']
        clientFormFactor = req_json['INNERTUBE_CONTEXT']['client']['clientFormFactor']
        appInstallData = req_json['INNERTUBE_CONTEXT']['client']['configInfo']['appInstallData']
        browserName = req_json['INNERTUBE_CONTEXT']['client']['browserName']
        browserVersion = req_json['INNERTUBE_CONTEXT']['client']['browserVersion']
        acceptHeader = req_json['INNERTUBE_CONTEXT']['client']['acceptHeader']
        deviceExperimentId = req_json['INNERTUBE_CONTEXT']['client']['deviceExperimentId']
        clickTrackingParams = req_json['INNERTUBE_CONTEXT']['clickTracking']['clickTrackingParams']

        self.__innertubeApiKey = req_json['WEB_PLAYER_CONTEXT_CONFIGS'][
            'WEB_PLAYER_CONTEXT_CONFIG_ID_KEVLAR_WATCH']['innertubeApiKey']
        self.__visitorData = visitorData

        req_json = req.text.split('var ytInitialData = ')
        req_json = req_json[1].split(';</script>')[0]
        req_json = json.loads(req_json)
        for item in req_json['engagementPanels']:
            if 'sectionListRenderer' in item['engagementPanelSectionListRenderer']['content'].keys():
                continuation = item['engagementPanelSectionListRenderer']['content']['sectionListRenderer']['contents'][0]['itemSectionRenderer']['contents'][0]['continuationItemRenderer']['continuationEndpoint']['continuationCommand']['token']

        return {
            "context": {
                "client": {
                    "hl": hl,
                    "gl": gl,
                    "remoteHost": remoteHost,
                    "deviceMake": deviceMake,
                    "deviceModel": deviceModel,
                    "visitorData": visitorData,
                    "userAgent": userAgent,
                    "clientName": clientName,
                    "clientVersion": clientVersion,
                    "osName": osName,
                    "osVersion": osVersion,
                    "originalUrl": originalUrl,
                    "screenPixelDensity": 2,
                    "platform": platform,
                    "clientFormFactor": clientFormFactor,
                    "configInfo": {
                        "appInstallData": appInstallData
                    },
                    "screenDensityFloat": 2,
                    "userInterfaceTheme": "USER_INTERFACE_THEME_LIGHT",
                    "timeZone": "America/Sao_Paulo",
                    "browserName": browserName,
                    "browserVersion": browserVersion,
                    "acceptHeader": acceptHeader,
                    "deviceExperimentId": deviceExperimentId,
                    "screenWidthPoints": 397,
                    "screenHeightPoints": 772,
                    "utcOffsetMinutes": -180,
                    "mainAppWebInfo": {
                        "graftUrl": self.__video_url,
                        "webDisplayMode": "WEB_DISPLAY_MODE_BROWSER",
                        "isWebNativeShareAvailable": True
                    }
                },
                "user": {"lockedSafetyMode": False},
                "request": {
                    "useSsl": True,
                    "internalExperimentFlags": []
                },
                "clickTracking": {
                    "clickTrackingParams": clickTrackingParams
                },
                "adSignalsInfo": {
                    "params": [
                        {"key": "dt", "value": "1707780229493"},
                        {"key": "flash", "value": "0"},
                        {"key": "frm", "value": "0"},
                        {"key": "u_tz", "value": "-180"},
                        {"key": "u_his", "value": "5"},
                        {"key": "u_h", "value": "772"},
                        {"key": "u_w", "value": "397"},
                        {"key": "u_ah", "value": "772"},
                        {"key": "u_aw", "value": "397"},
                        {"key": "u_cd", "value": "24"},
                        {"key": "bc", "value": "31"},
                        {"key": "bih", "value": "757"},
                        {"key": "biw", "value": "382"},
                        {"key": "brdim", "value": "0,0,0,0,397,0,397,772,397,772"},
                        {"key": "vis", "value": "1"},
                        {"key": "wgl", "value": "true"},
                        {"key": "ca_type", "value": "image"}
                    ]
                }
            },
            "continuation": continuation
        }

    def __check_if_first_pagination(self, data: dict) -> tuple:
        '''
        Check if the data contains `reloadContinuationItemsCommand` or `appendContinuationItemsAction`
        Return ('is first pagination?','a valid key')
        'is first pagination?' is true if first pagination or false if other pagination
        'valid key' can be ['onResponseReceivedEndpoints'][-1]['reloadContinuationItemsCommand'] for example
        '''
        if 'reloadContinuationItemsCommand' in data.keys():
            return (True, data['reloadContinuationItemsCommand'])
        elif 'appendContinuationItemsAction' in data.keys():
            return (False, data['appendContinuationItemsAction'])

    def __get_comments(self, data: dict) -> dict:

        base_url = 'https://www.youtube.com/youtubei/v1/next?key='
        header = {
            'Content-Type': 'application/json',
            'Sec-Fetch-Dest': 'empty',
            'Accept': '*/*',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'same-origin',
            'Host': 'www.youtube.com',
            'Origin': 'https://www.youtube.com',
            'Referer': self.__video_url,
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.2.1 Safari/605.1.15',
            'Content-Length': '2599',
            'Connection': 'keep-alive',
            'X-Youtube-Client-Version': '2.20240210.05.00',
            'X-Youtube-Client-Name': '1',
            'Priority': 'u=3, i',
            'X-Goog-Visitor-Id': self.__visitorData,
            'X-Youtube-Bootstrap-Logged-In': 'false',
        }
        # request
        req = self.__session.post(
            base_url+self.__innertubeApiKey, json=data, headers=header)
        req_json = req.json()

        # check if response contains comments section
        _, pagination = self.__check_if_first_pagination(
            req_json['onResponseReceivedEndpoints'][-1])
        if pagination['targetId'] != 'comments-section' and pagination['targetId'] != 'engagement-panel-comments-section' and pagination['targetId'] in 'comment-replies-item-':
            raise Exception('The data is not a comment content.')

        # get comments and check them
        comments = pagination['continuationItems']
        self.__check_comments(comments)

        # check continuation
        if 'continuationItemRenderer' in comments[-1].keys():
            data = self.__initial_data
            try:
                # continuation for commom pagination
                data['context']['clickTrackingParams'] = comments[-1]['continuationItemRenderer']['continuationEndpoint']['clickTrackingParams']
                data['continuation'] = comments[-1]['continuationItemRenderer']['continuationEndpoint']['continuationCommand']['token']
            except KeyError:
                # continuation when there is lots of replies
                data['context']['clickTrackingParams'] = comments[-1]['continuationItemRenderer']['button']['buttonRenderer']['command']['clickTrackingParams']
                data['continuation'] = comments[-1]['continuationItemRenderer']['button']['buttonRenderer']['command']['continuationCommand']['token']

            self.__get_comments(data)

    def __check_comments(self, comments: list):
        for comment in comments:
            # check if item is really a comment or a continuation item
            if 'continuationItemRenderer' in comment.keys():
                break
            self.__save_comment(comment)
            # check for replies
            try:
                if 'replies' in comment['commentThreadRenderer']:
                    data = self.__initial_data
                    data['context']['clickTrackingParams'] = comment['commentThreadRenderer']['replies']['commentRepliesRenderer'][
                        'contents'][0]['continuationItemRenderer']['continuationEndpoint']['clickTrackingParams']
                    data['continuation'] = comment['commentThreadRenderer']['replies']['commentRepliesRenderer'][
                        'contents'][0]['continuationItemRenderer']['continuationEndpoint']['continuationCommand']['token']
                    self.__get_comments(data)
            except KeyError:
                pass

    def __save_comment(self, comment: dict):
        # check if comment is a thread or a simple comment (like a reply)
        if 'commentThreadRenderer' in comment.keys():
            comment = comment['commentThreadRenderer']['comment']['commentRenderer']
        elif 'commentRenderer' in comment.keys():
            comment = comment['commentRenderer']
        else:
            raise Exception('Comment type not recognized.')

        text = ''
        for item in comment['contentText']['runs']:
            text += item['text']

        try:
            author = comment['authorText']['simpleText']
        except KeyError:
            # for some reason sometimes the author is not visible
            author = None

        comment_id = comment['commentId']
        reply = True if comment_id.find('.') != -1 else False

        df = pd.DataFrame({'commentId': comment_id, 'author': [
                          author], 'text': [text], 'reply': [reply]})

        self.__comments_df = pd.concat([self.__comments_df, df])


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Save Youtube comments from specific video.')
    parser.add_argument('url', help='URL of video')
    parser.add_argument('output', help='Output file')
    args = parser.parse_args()

    try:
        ytcomments = YoutubeCommentsExtractor()
        ytcomments.extract(args.url, args.output)
    except Exception as e:
        logger.setLevel(logging.ERROR)
        logger.error(e)