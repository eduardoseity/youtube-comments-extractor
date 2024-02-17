**URL**
>https://www.youtube.com/youtubei/v1/next?key={innertubeApiKey}

**METHOD**
`POST`

**BODY**
```json
{
    "context": {
        "client": {
            "hl": "hl",
            "gl": "gl",
            "remoteHost": "remoteHost",
            "deviceMake": "deviceMake",
            "deviceModel": "deviceModel",
            "visitorData": "visitorData",
            "userAgent": "userAgent",
            "clientName": "clientName",
            "clientVersion": "clientVersion",
            "osName": "osName",
            "osVersion": "osVersion",
            "originalUrl": "originalUrl",
            "screenPixelDensity": 2,
            "platform": "platform",
            "clientFormFactor": "clientFormFactor",
            "configInfo": {
                "appInstallData": "appInstallData"
            },
            "screenDensityFloat": 2,
            "userInterfaceTheme": "USER_INTERFACE_THEME_LIGHT",
            "timeZone": "America/Sao_Paulo",
            "browserName": "browserName",
            "browserVersion": "browserVersion",
            "acceptHeader": "acceptHeader",
            "deviceExperimentId": "deviceExperimentId",
            "screenWidthPoints": 397,
            "screenHeightPoints": 772,
            "utcOffsetMinutes": -180,
            "mainAppWebInfo": {
                "graftUrl": "video_url",
                "webDisplayMode": "WEB_DISPLAY_MODE_BROWSER",
                "isWebNativeShareAvailable": "True"
            }
        },
        "user": {
            "lockedSafetyMode": "False"
        },
        "request": {
            "useSsl": "True",
            "internalExperimentFlags": []
        },
        "clickTracking": {
            "clickTrackingParams": "clickTrackingParams"
        },
        "adSignalsInfo": {
            "params": [
                {
                    "key": "dt",
                    "value": "1707780229493"
                },
                {
                    "key": "flash",
                    "value": "0"
                },
                {
                    "key": "frm",
                    "value": "0"
                },
                {
                    "key": "u_tz",
                    "value": "-180"
                },
                {
                    "key": "u_his",
                    "value": "5"
                },
                {
                    "key": "u_h",
                    "value": "772"
                },
                {
                    "key": "u_w",
                    "value": "397"
                },
                {
                    "key": "u_ah",
                    "value": "772"
                },
                {
                    "key": "u_aw",
                    "value": "397"
                },
                {
                    "key": "u_cd",
                    "value": "24"
                },
                {
                    "key": "bc",
                    "value": "31"
                },
                {
                    "key": "bih",
                    "value": "757"
                },
                {
                    "key": "biw",
                    "value": "382"
                },
                {
                    "key": "brdim",
                    "value": "0,0,0,0,397,0,397,772,397,772"
                },
                {
                    "key": "vis",
                    "value": "1"
                },
                {
                    "key": "wgl",
                    "value": "true"
                },
                {
                    "key": "ca_type",
                    "value": "image"
                }
            ]
        }
    },
    "continuation": "continuation"
}
```

**MAIN KEYS**
>(array) **`onResponseReceivedEndpoints`**: here is where the data received are. <br>When the key `reloadContinuationItemsCommand` is present means that the data received is the first pagination, when the key `appendContinuationItemsAction` is present means that the data received is not the first pagination.<br>When the length of this array is equal 2 the first item will contain the comments' header info, and the second one will contain the comments contents.

>(string) **`onResponseReceivedEndpoints[n].clickTrackingParams`**: ID of received endpoint

>(string) **`onResponseReceivedEndpoints[n].reloadContinuationItemsCommand.slot`**: only valid for **first pagination**, the others will not contain this key
>* When `slot=RELOAD_CONTINUATION_SLOT_HEADER` the item will contain the information of comments' header, like number of comments. The number of comments could be accessed by `onResponseReceivedEndpoints[0].reloadContinuationItemsCommand.continuationItems[0].commentsHeaderRenderer.countText.runs[0].text` for example.
>* When `slot=RELOAD_CONTINUATION_SLOT_BODY` the item will contain the contents of comments

>(array) **`onResponseReceivedEndpoints[n_last].reloadContinuationItemsCommand.continuationItems`**
or
(array) **`onResponseReceivedEndpoints[n_last].appendContinuationItemsAction.continuationItems`**
Contains objects with `commentThreadRenderer` key which the value represents the data of the comment
>* `.commentThreadRenderer.comment.commentRenderer.authorText.simpleText`: the user of comment's author
>* `.commentThreadRenderer.comment.commentRenderer.authorThumbnail.thumbnails`: the author's thumbnail
>* `.commentThreadRenderer.comment.commentRenderer.contentText.runs`: an array containing the texts of the comment, to show the entire text as shown in the web you will need to concatenate all **`text`** key's value of this array.

>(object) **`onResponseReceivedEndpoints[n_last].reloadContinuationItemsCommand.continuationItems[n_last].continuationItemRenderer`** when this key is present means that there is a continuation 
or
(object) **`onResponseReceivedEndpoints[n_last].appendContinuationItemsAction.continuationItems[n_last].continuationItemRenderer`**
When this key is present means that there is a continuation to be shown in pagination

>(string) **`onResponseReceivedEndpoints[n_last].reloadContinuationItemsCommand.targetId`**
or
(string) **`onResponseReceivedEndpoints[n_last].appendContinuationItemsAction.targetId`**
When `targetId=comments-section` or `targetId=engagement-panel-comments-section` means that the contents are comments, when `targetId=watch-next-feed` means that the contents are video recommendation.<br>
When `targetId=comment-replies-item-{commentId}` means that the comment is a reply to another comment identified by *commentId*

>(string) **`onResponseReceivedEndpoints[n_last].reloadContinuationItemsCommand.continuationItems[n].commentThreadRenderer.replies`**
or
(string) **`onResponseReceivedEndpoints[n_last].appendContinuationItemsAction.continuationItems[n].commentThreadRenderer.replies`**
When the key is present means that the comment has replies

