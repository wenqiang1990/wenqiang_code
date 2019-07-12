#在线生成schema：https://jsonschema.net/
#jsonschema验证方法：https://blog.csdn.net/junli_chen/article/details/52965763
#https://blog.csdn.net/m0_37920188/article/details/72846226
schema = {
        "definitions": {},
        "$schema": "http://json-schema.org/draft-07/schema#",
        "$id": "http://example.com/root.json",
        "type": "object",
        "title": "The Root Schema",
        "required": [
            "statusCode",
            "playerUrls",
            "liveData"
        ],
        "properties": {
            "statusCode": {
                "$id": "#/properties/statusCode",
                "type": "string",
                "title": "The Statuscode Schema",
                "default": "",
                "examples": [
                    "000000"
                ],
                "pattern": "^(.*)$"
            },
            "playerUrls": {
                "$id": "#/properties/playerUrls",
                "type": "object",
                "title": "The Playerurls Schema",
                "required": [
                    "rtmp",
                    "hls",
                    "flv"
                ],
                "properties": {
                    "rtmp": {
                        "$id": "#/properties/playerUrls/properties/rtmp",
                        "type": "object",
                        "title": "The Rtmp Schema",
                        "required": [
                            "source"
                        ],
                        "properties": {
                            "source": {
                                "$id": "#/properties/playerUrls/properties/rtmp/properties/source",
                                "type": "string",
                                "title": "The Source Schema",
                                "default": "",
                                "examples": [
                                    "rtmp://124.206.192.31:1936/ff8080815dbc080c015dbc9d7cd40003/1554197353659?auth=f5442859bb99-0&uuid=1b873fc5130f4fc29db3f26d7e6e89eb"
                                ],
                                "pattern": "^(.*)$"
                            }
                        }
                    },
                    "hls": {
                        "$id": "#/properties/playerUrls/properties/hls",
                        "type": "object",
                        "title": "The Hls Schema",
                        "required": [
                            "source"
                        ],
                        "properties": {
                            "source": {
                                "$id": "#/properties/playerUrls/properties/hls/properties/source",
                                "type": "string",
                                "title": "The Source Schema",
                                "default": "",
                                "examples": [
                                    "http://124.206.192.31/hls/ff8080815dbc080c015dbc9d7cd40003/1554197353659.m3u8?auth=f5442859bb99-0&uuid=7c5329b7a3d443729ed694d2f16fbecb"
                                ],
                                "pattern": "^(.*)$"
                            }
                        }
                    },
                    "flv": {
                        "$id": "#/properties/playerUrls/properties/flv",
                        "type": "object",
                        "title": "The Flv Schema",
                        "required": [
                            "source"
                        ],
                        "properties": {
                            "source": {
                                "$id": "#/properties/playerUrls/properties/flv/properties/source",
                                "type": "string",
                                "title": "The Source Schema",
                                "default": "",
                                "examples": [
                                    "http://124.206.192.31/ff8080815dbc080c015dbc9d7cd40003/1554197353659.flv?auth=f5442859bb99-0&uuid=9ef0fb82528f40a491fd4edc7bf4565b"
                                ],
                                "pattern": "^(.*)$"
                            }
                        }
                    }
                }
            },
            "liveData": {
                "$id": "#/properties/liveData",
                "type": "array",
                "title": "The Livedata Schema",
                "items": {
                    "$id": "#/properties/liveData/items",
                    "type": "object",
                    "title": "The Items Schema",
                    "required": [
                        "sessionId",
                        "playData"
                    ],
                    "properties": {
                        "sessionId": {
                            "$id": "#/properties/liveData/items/properties/sessionId",
                            "type": "string",
                            "title": "The Sessionid Schema",
                            "default": "",
                            "examples": [
                                "LIVE20190402172913617"
                            ],
                            "pattern": "^(.*)$"
                        },
                        "playData": {
                            "$id": "#/properties/liveData/items/properties/playData",
                            "type": "object",
                            "title": "The Playdata Schema",
                            "required": [
                                "playUrls",
                                "backupLinkNode"
                            ],
                            "properties": {
                                "playUrls": {
                                    "$id": "#/properties/liveData/items/properties/playData/properties/playUrls",
                                    "type": "object",
                                    "title": "The Playurls Schema",
                                    "required": [
                                        "rtmp",
                                        "hls",
                                        "flv"
                                    ],
                                    "properties": {
                                        "rtmp": {
                                            "$id": "#/properties/liveData/items/properties/playData/properties/playUrls/properties/rtmp",
                                            "type": "object",
                                            "title": "The Rtmp Schema",
                                            "required": [
                                                "source"
                                            ],
                                            "properties": {
                                                "source": {
                                                    "$id": "#/properties/liveData/items/properties/playData/properties/playUrls/properties/rtmp/properties/source",
                                                    "type": "string",
                                                    "title": "The Source Schema",
                                                    "default": "",
                                                    "examples": [
                                                        "rtmp://124.206.192.31:1936/ff8080815dbc080c015dbc9d7cd40003/1554197353659?auth=f5442859bb99-0&uuid=1b873fc5130f4fc29db3f26d7e6e89eb"
                                                    ],
                                                    "pattern": "^(.*)$"
                                                }
                                            }
                                        },
                                        "hls": {
                                            "$id": "#/properties/liveData/items/properties/playData/properties/playUrls/properties/hls",
                                            "type": "object",
                                            "title": "The Hls Schema",
                                            "required": [
                                                "source"
                                            ],
                                            "properties": {
                                                "source": {
                                                    "$id": "#/properties/liveData/items/properties/playData/properties/playUrls/properties/hls/properties/source",
                                                    "type": "string",
                                                    "title": "The Source Schema",
                                                    "default": "",
                                                    "examples": [
                                                        "http://124.206.192.31/hls/ff8080815dbc080c015dbc9d7cd40003/1554197353659.m3u8?auth=f5442859bb99-0&uuid=7c5329b7a3d443729ed694d2f16fbecb"
                                                    ],
                                                    "pattern": "^(.*)$"
                                                }
                                            }
                                        },
                                        "flv": {
                                            "$id": "#/properties/liveData/items/properties/playData/properties/playUrls/properties/flv",
                                            "type": "object",
                                            "title": "The Flv Schema",
                                            "required": [
                                                "source"
                                            ],
                                            "properties": {
                                                "source": {
                                                    "$id": "#/properties/liveData/items/properties/playData/properties/playUrls/properties/flv/properties/source",
                                                    "type": "string",
                                                    "title": "The Source Schema",
                                                    "default": "",
                                                    "examples": [
                                                        "http://124.206.192.31/ff8080815dbc080c015dbc9d7cd40003/1554197353659.flv?auth=f5442859bb99-0&uuid=9ef0fb82528f40a491fd4edc7bf4565b"
                                                    ],
                                                    "pattern": "^(.*)$"
                                                }
                                            }
                                        }
                                    }
                                },
                                "backupLinkNode": {
                                    "$id": "#/properties/liveData/items/properties/playData/properties/backupLinkNode",
                                    "type": "object",
                                    "title": "The Backuplinknode Schema",
                                    "required": [
                                        "rtmp",
                                        "hls",
                                        "flv"
                                    ],
                                    "properties": {
                                        "rtmp": {
                                            "$id": "#/properties/liveData/items/properties/playData/properties/backupLinkNode/properties/rtmp",
                                            "type": "object",
                                            "title": "The Rtmp Schema",
                                            "required": [
                                                "source"
                                            ],
                                            "properties": {
                                                "source": {
                                                    "$id": "#/properties/liveData/items/properties/playData/properties/backupLinkNode/properties/rtmp/properties/source",
                                                    "type": "object",
                                                    "title": "The Source Schema"
                                                }
                                            }
                                        },
                                        "hls": {
                                            "$id": "#/properties/liveData/items/properties/playData/properties/backupLinkNode/properties/hls",
                                            "type": "object",
                                            "title": "The Hls Schema",
                                            "required": [
                                                "source"
                                            ],
                                            "properties": {
                                                "source": {
                                                    "$id": "#/properties/liveData/items/properties/playData/properties/backupLinkNode/properties/hls/properties/source",
                                                    "type": "object",
                                                    "title": "The Source Schema"
                                                }
                                            }
                                        },
                                        "flv": {
                                            "$id": "#/properties/liveData/items/properties/playData/properties/backupLinkNode/properties/flv",
                                            "type": "object",
                                            "title": "The Flv Schema",
                                            "required": [
                                                "source"
                                            ],
                                            "properties": {
                                                "source": {
                                                    "$id": "#/properties/liveData/items/properties/playData/properties/backupLinkNode/properties/flv/properties/source",
                                                    "type": "object",
                                                    "title": "The Source Schema"
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }