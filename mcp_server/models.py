# generated by fastapi-codegen:
#   filename:  openapi.yaml
#   timestamp: 2025-06-28T12:11:57+00:00

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Field, RootModel, SecretStr, conint, constr


class AccessDeniedException(RootModel[Any]):
    root: Any


class Boolean(RootModel[bool]):
    root: bool


class ChannelArn(
    RootModel[
        constr(
            pattern=r'^arn:aws:[is]vs:[a-z0-9-]+:[0-9]+:channel/[a-zA-Z0-9-]+$',
            min_length=1,
            max_length=128,
        )
    ]
):
    root: constr(
        pattern=r'^arn:aws:[is]vs:[a-z0-9-]+:[0-9]+:channel/[a-zA-Z0-9-]+$',
        min_length=1,
        max_length=128,
    )


class ChannelArnList(RootModel[List[ChannelArn]]):
    root: List[ChannelArn] = Field(..., max_length=50, min_length=1)


class ChannelLatencyMode(Enum):
    NORMAL = 'NORMAL'
    LOW = 'LOW'


class ChannelName(
    RootModel[constr(pattern=r'^[a-zA-Z0-9-_]*$', min_length=0, max_length=128)]
):
    root: constr(pattern=r'^[a-zA-Z0-9-_]*$', min_length=0, max_length=128)


class ChannelNotBroadcasting(RootModel[Any]):
    root: Any


class ChannelRecordingConfigurationArn(
    RootModel[
        constr(
            pattern=r'^$|^arn:aws:ivs:[a-z0-9-]+:[0-9]+:recording-configuration/[a-zA-Z0-9-]+$',
            min_length=0,
            max_length=128,
        )
    ]
):
    root: constr(
        pattern=r'^$|^arn:aws:ivs:[a-z0-9-]+:[0-9]+:recording-configuration/[a-zA-Z0-9-]+$',
        min_length=0,
        max_length=128,
    )


class ChannelType(Enum):
    BASIC = 'BASIC'
    STANDARD = 'STANDARD'


class ConflictException(RootModel[Any]):
    root: Any


class DeleteChannelRequest(BaseModel):
    arn: ChannelArn


class DeletePlaybackKeyPairResponse(BaseModel):
    pass


class GetChannelRequest(BaseModel):
    arn: ChannelArn


class GetStreamRequest(BaseModel):
    channelArn: ChannelArn


class IngestEndpoint(RootModel[str]):
    root: str


class InsecureIngest(RootModel[bool]):
    root: bool


class Integer(RootModel[int]):
    root: int


class InternalServerException(RootModel[Any]):
    root: Any


class IsAuthorized(RootModel[bool]):
    root: bool


class ListTagsForResourceRequest(BaseModel):
    pass


class MaxChannelResults(RootModel[conint(ge=1, le=100)]):
    root: conint(ge=1, le=100)


class MaxPlaybackKeyPairResults(RootModel[conint(ge=1, le=100)]):
    root: conint(ge=1, le=100)


class MaxRecordingConfigurationResults(RootModel[conint(ge=1, le=100)]):
    root: conint(ge=1, le=100)


class MaxStreamKeyResults(RootModel[conint(ge=1, le=50)]):
    root: conint(ge=1, le=50)


class MaxStreamResults(RootModel[conint(ge=1, le=100)]):
    root: conint(ge=1, le=100)


class PaginationToken(
    RootModel[constr(pattern=r'^[a-zA-Z0-9+/=_-]*$', min_length=0, max_length=1024)]
):
    root: constr(pattern=r'^[a-zA-Z0-9+/=_-]*$', min_length=0, max_length=1024)


class PendingVerification(RootModel[Any]):
    root: Any


class PlaybackKeyPairArn(
    RootModel[
        constr(
            pattern=r'^arn:aws:[is]vs:[a-z0-9-]+:[0-9]+:playback-key/[a-zA-Z0-9-]+$',
            min_length=1,
            max_length=128,
        )
    ]
):
    root: constr(
        pattern=r'^arn:aws:[is]vs:[a-z0-9-]+:[0-9]+:playback-key/[a-zA-Z0-9-]+$',
        min_length=1,
        max_length=128,
    )


class PlaybackKeyPairFingerprint(RootModel[str]):
    root: str


class PlaybackKeyPairName(
    RootModel[constr(pattern=r'^[a-zA-Z0-9-_]*$', min_length=0, max_length=128)]
):
    root: constr(pattern=r'^[a-zA-Z0-9-_]*$', min_length=0, max_length=128)


class PlaybackPublicKeyMaterial(RootModel[str]):
    root: str


class PlaybackURL(RootModel[str]):
    root: str


class RecordingConfigurationArn(
    RootModel[
        constr(
            pattern=r'^arn:aws:ivs:[a-z0-9-]+:[0-9]+:recording-configuration/[a-zA-Z0-9-]+$',
            min_length=0,
            max_length=128,
        )
    ]
):
    root: constr(
        pattern=r'^arn:aws:ivs:[a-z0-9-]+:[0-9]+:recording-configuration/[a-zA-Z0-9-]+$',
        min_length=0,
        max_length=128,
    )


class RecordingConfigurationName(
    RootModel[constr(pattern=r'^[a-zA-Z0-9-_]*$', min_length=0, max_length=128)]
):
    root: constr(pattern=r'^[a-zA-Z0-9-_]*$', min_length=0, max_length=128)


class RecordingConfigurationState(Enum):
    CREATING = 'CREATING'
    CREATE_FAILED = 'CREATE_FAILED'
    ACTIVE = 'ACTIVE'


class RecordingMode(Enum):
    DISABLED = 'DISABLED'
    INTERVAL = 'INTERVAL'


class RecordingReconnectWindowSeconds(RootModel[conint(ge=0, le=300)]):
    root: conint(ge=0, le=300)


class ResourceArn(
    RootModel[
        constr(
            pattern=r'^arn:aws:[is]vs:[a-z0-9-]+:[0-9]+:[a-z-]/[a-zA-Z0-9-]+$',
            min_length=1,
            max_length=128,
        )
    ]
):
    root: constr(
        pattern=r'^arn:aws:[is]vs:[a-z0-9-]+:[0-9]+:[a-z-]/[a-zA-Z0-9-]+$',
        min_length=1,
        max_length=128,
    )


class ResourceNotFoundException(RootModel[Any]):
    root: Any


class S3DestinationBucketName(
    RootModel[constr(pattern=r'^[a-z0-9-.]+$', min_length=3, max_length=63)]
):
    root: constr(pattern=r'^[a-z0-9-.]+$', min_length=3, max_length=63)


class S3DestinationConfiguration(BaseModel):
    bucketName: S3DestinationBucketName


class ServiceQuotaExceededException(RootModel[Any]):
    root: Any


class StopStreamRequest(BaseModel):
    channelArn: ChannelArn


class StopStreamResponse(BaseModel):
    pass


class StreamHealth(Enum):
    HEALTHY = 'HEALTHY'
    STARVING = 'STARVING'
    UNKNOWN = 'UNKNOWN'


class StreamId(
    RootModel[constr(pattern=r'^st-[a-zA-Z0-9]+$', min_length=26, max_length=26)]
):
    root: constr(pattern=r'^st-[a-zA-Z0-9]+$', min_length=26, max_length=26)


class StreamKeyArn(
    RootModel[
        constr(
            pattern=r'^arn:aws:[is]vs:[a-z0-9-]+:[0-9]+:stream-key/[a-zA-Z0-9-]+$',
            min_length=1,
            max_length=128,
        )
    ]
):
    root: constr(
        pattern=r'^arn:aws:[is]vs:[a-z0-9-]+:[0-9]+:stream-key/[a-zA-Z0-9-]+$',
        min_length=1,
        max_length=128,
    )


class StreamKeyArnList(RootModel[List[StreamKeyArn]]):
    root: List[StreamKeyArn] = Field(..., max_length=50, min_length=1)


class StreamKeyValue(RootModel[SecretStr]):
    root: SecretStr


class StreamMetadata(RootModel[SecretStr]):
    root: SecretStr


class StreamStartTime(RootModel[datetime]):
    root: datetime


class StreamState(Enum):
    LIVE = 'LIVE'
    OFFLINE = 'OFFLINE'


class StreamUnavailable(RootModel[Any]):
    root: Any


class StreamViewerCount(RootModel[int]):
    root: int


class String(RootModel[str]):
    root: str


class TagKey(RootModel[constr(min_length=1, max_length=128)]):
    root: constr(min_length=1, max_length=128)


class TagKeyList(RootModel[List[TagKey]]):
    root: List[TagKey] = Field(..., max_length=50, min_length=0)


class TagResourceResponse(BaseModel):
    pass


class TagValue(RootModel[constr(min_length=0, max_length=256)]):
    root: constr(min_length=0, max_length=256)


class Tags(RootModel[Optional[Dict[str, TagValue]]]):
    root: Optional[Dict[str, TagValue]] = None


class TargetIntervalSeconds(RootModel[conint(ge=1, le=60)]):
    root: conint(ge=1, le=60)


class ThrottlingException(RootModel[Any]):
    root: Any


class ThumbnailConfiguration(BaseModel):
    recordingMode: Optional[RecordingMode] = None
    targetIntervalSeconds: Optional[TargetIntervalSeconds] = None


class Time(RootModel[datetime]):
    root: datetime


class UntagResourceRequest(BaseModel):
    pass


class UntagResourceResponse(BaseModel):
    pass


class UpdateChannelRequest(BaseModel):
    arn: ChannelArn
    authorized: Optional[Boolean] = None
    insecureIngest: Optional[Boolean] = None
    latencyMode: Optional[ChannelLatencyMode] = None
    name: Optional[ChannelName] = None
    recordingConfigurationArn: Optional[ChannelRecordingConfigurationArn] = None
    type: Optional[ChannelType] = None


class ValidationException(RootModel[Any]):
    root: Any


class VideoConfiguration(BaseModel):
    avcLevel: Optional[String] = None
    avcProfile: Optional[String] = None
    codec: Optional[String] = None
    encoder: Optional[String] = None
    targetBitrate: Optional[Integer] = None
    targetFramerate: Optional[Integer] = None
    videoHeight: Optional[Integer] = None
    videoWidth: Optional[Integer] = None


class ErrorCode(RootModel[str]):
    root: str


class ErrorMessage(RootModel[str]):
    root: str


class BatchGetChannelPostRequest(BaseModel):
    arns: List[ChannelArn] = Field(
        ..., description='Array of ARNs, one per channel.', max_length=50, min_length=1
    )


class BatchGetStreamKeyPostRequest(BaseModel):
    arns: List[StreamKeyArn] = Field(
        ...,
        description='Array of ARNs, one per stream key.',
        max_length=50,
        min_length=1,
    )


class LatencyMode(Enum):
    NORMAL = 'NORMAL'
    LOW = 'LOW'


class Type(Enum):
    BASIC = 'BASIC'
    STANDARD = 'STANDARD'


class CreateChannelPostRequest(BaseModel):
    authorized: Optional[bool] = Field(
        None,
        description='Whether the channel is private (enabled for playback authorization). Default: <code>false</code>.',
    )
    insecureIngest: Optional[bool] = Field(
        None,
        description='Whether the channel allows insecure RTMP ingest. Default: <code>false</code>.',
    )
    latencyMode: Optional[LatencyMode] = Field(
        None,
        description='Channel latency mode. Use <code>NORMAL</code> to broadcast and deliver live video up to Full HD. Use <code>LOW</code> for near-real-time interaction with viewers. (Note: In the Amazon IVS console, <code>LOW</code> and <code>NORMAL</code> correspond to Ultra-low and Standard, respectively.) Default: <code>LOW</code>.',
    )
    name: Optional[
        constr(pattern=r'^[a-zA-Z0-9-_]*$', min_length=0, max_length=128)
    ] = Field(None, description='Channel name.')
    recordingConfigurationArn: Optional[
        constr(
            pattern=r'^$|^arn:aws:ivs:[a-z0-9-]+:[0-9]+:recording-configuration/[a-zA-Z0-9-]+$',
            min_length=0,
            max_length=128,
        )
    ] = Field(
        None,
        description='Recording-configuration ARN. Default: "" (empty string, recording is disabled).',
    )
    tags: Optional[Dict[str, TagValue]] = Field(
        None,
        description='Array of 1-50 maps, each of the form <code>string:string (key:value)</code>. See <a href="https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html">Tagging Amazon Web Services Resources</a> for more information, including restrictions that apply to tags and "Tag naming limits and requirements"; Amazon IVS has no service-specific constraints beyond what is documented there.',
    )
    type: Optional[Type] = Field(
        None,
        description='<p>Channel type, which determines the allowable resolution and bitrate. <i>If you exceed the allowable resolution or bitrate, the stream probably will disconnect immediately.</i> Default: <code>STANDARD</code>. Valid values:</p> <ul> <li> <p> <code>STANDARD</code>: Video is transcoded: multiple qualities are generated from the original input, to automatically give viewers the best experience for their devices and network conditions. Transcoding allows higher playback quality across a range of download speeds. Resolution can be up to 1080p and bitrate can be up to 8.5 Mbps. Audio is transcoded only for renditions 360p and below; above that, audio is passed through. This is the default.</p> </li> <li> <p> <code>BASIC</code>: Video is transmuxed: Amazon IVS delivers the original input to viewers. The viewer’s video-quality choice is limited to the original input. Resolution can be up to 1080p and bitrate can be up to 1.5 Mbps for 480p and up to 3.5 Mbps for resolutions between 480p and 1080p.</p> </li> </ul>',
    )


class DestinationConfiguration(BaseModel):
    s3: Optional[S3DestinationConfiguration] = None


class CreateRecordingConfigurationPostRequest(BaseModel):
    destinationConfiguration: DestinationConfiguration = Field(
        ...,
        description='A complex type that describes a location where recorded videos will be stored. Each member represents a type of destination configuration. For recording, you define one and only one type of destination configuration.',
    )
    name: Optional[
        constr(pattern=r'^[a-zA-Z0-9-_]*$', min_length=0, max_length=128)
    ] = Field(
        None,
        description='Recording-configuration name. The value does not need to be unique.',
    )
    recordingReconnectWindowSeconds: Optional[conint(ge=0, le=300)] = Field(
        None,
        description='If a broadcast disconnects and then reconnects within the specified interval, the multiple streams will be considered a single broadcast and merged together. Default: 0.',
    )
    tags: Optional[Dict[str, TagValue]] = Field(
        None,
        description='Array of 1-50 maps, each of the form <code>string:string (key:value)</code>. See <a href="https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html">Tagging Amazon Web Services Resources</a> for more information, including restrictions that apply to tags and "Tag naming limits and requirements"; Amazon IVS has no service-specific constraints beyond what is documented there.',
    )
    thumbnailConfiguration: Optional[ThumbnailConfiguration] = Field(
        None,
        description='An object representing a configuration of thumbnails for recorded video.',
    )


class CreateStreamKeyPostRequest(BaseModel):
    channelArn: constr(
        pattern=r'^arn:aws:[is]vs:[a-z0-9-]+:[0-9]+:channel/[a-zA-Z0-9-]+$',
        min_length=1,
        max_length=128,
    ) = Field(..., description='ARN of the channel for which to create the stream key.')
    tags: Optional[Dict[str, TagValue]] = Field(
        None,
        description='Array of 1-50 maps, each of the form <code>string:string (key:value)</code>. See <a href="https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html">Tagging Amazon Web Services Resources</a> for more information, including restrictions that apply to tags and "Tag naming limits and requirements"; Amazon IVS has no service-specific constraints beyond what is documented there.',
    )


class DeleteChannelPostRequest(BaseModel):
    arn: constr(
        pattern=r'^arn:aws:[is]vs:[a-z0-9-]+:[0-9]+:channel/[a-zA-Z0-9-]+$',
        min_length=1,
        max_length=128,
    ) = Field(..., description='ARN of the channel to be deleted.')


class DeletePlaybackKeyPairPostRequest(BaseModel):
    arn: constr(
        pattern=r'^arn:aws:[is]vs:[a-z0-9-]+:[0-9]+:playback-key/[a-zA-Z0-9-]+$',
        min_length=1,
        max_length=128,
    ) = Field(..., description='ARN of the key pair to be deleted.')


class DeleteRecordingConfigurationPostRequest(BaseModel):
    arn: constr(
        pattern=r'^arn:aws:ivs:[a-z0-9-]+:[0-9]+:recording-configuration/[a-zA-Z0-9-]+$',
        min_length=0,
        max_length=128,
    ) = Field(..., description='ARN of the recording configuration to be deleted.')


class DeleteStreamKeyPostRequest(BaseModel):
    arn: constr(
        pattern=r'^arn:aws:[is]vs:[a-z0-9-]+:[0-9]+:stream-key/[a-zA-Z0-9-]+$',
        min_length=1,
        max_length=128,
    ) = Field(..., description='ARN of the stream key to be deleted.')


class GetChannelPostRequest(BaseModel):
    arn: constr(
        pattern=r'^arn:aws:[is]vs:[a-z0-9-]+:[0-9]+:channel/[a-zA-Z0-9-]+$',
        min_length=1,
        max_length=128,
    ) = Field(
        ...,
        description='ARN of the channel for which the configuration is to be retrieved.',
    )


class GetPlaybackKeyPairPostRequest(BaseModel):
    arn: constr(
        pattern=r'^arn:aws:[is]vs:[a-z0-9-]+:[0-9]+:playback-key/[a-zA-Z0-9-]+$',
        min_length=1,
        max_length=128,
    ) = Field(..., description='ARN of the key pair to be returned.')


class GetRecordingConfigurationPostRequest(BaseModel):
    arn: constr(
        pattern=r'^arn:aws:ivs:[a-z0-9-]+:[0-9]+:recording-configuration/[a-zA-Z0-9-]+$',
        min_length=0,
        max_length=128,
    ) = Field(..., description='ARN of the recording configuration to be retrieved.')


class GetStreamPostRequest(BaseModel):
    channelArn: constr(
        pattern=r'^arn:aws:[is]vs:[a-z0-9-]+:[0-9]+:channel/[a-zA-Z0-9-]+$',
        min_length=1,
        max_length=128,
    ) = Field(..., description='Channel ARN for stream to be accessed.')


class GetStreamKeyPostRequest(BaseModel):
    arn: constr(
        pattern=r'^arn:aws:[is]vs:[a-z0-9-]+:[0-9]+:stream-key/[a-zA-Z0-9-]+$',
        min_length=1,
        max_length=128,
    ) = Field(..., description='ARN for the stream key to be retrieved.')


class GetStreamSessionPostRequest(BaseModel):
    channelArn: constr(
        pattern=r'^arn:aws:[is]vs:[a-z0-9-]+:[0-9]+:channel/[a-zA-Z0-9-]+$',
        min_length=1,
        max_length=128,
    ) = Field(..., description='ARN of the channel resource')
    streamId: Optional[
        constr(pattern=r'^st-[a-zA-Z0-9]+$', min_length=26, max_length=26)
    ] = Field(
        None,
        description='Unique identifier for a live or previously live stream in the specified channel. If no <code>streamId</code> is provided, this returns the most recent stream session for the channel, if it exists.',
    )


class ImportPlaybackKeyPairPostRequest(BaseModel):
    name: Optional[
        constr(pattern=r'^[a-zA-Z0-9-_]*$', min_length=0, max_length=128)
    ] = Field(
        None,
        description='Playback-key-pair name. The value does not need to be unique.',
    )
    publicKeyMaterial: str = Field(
        ..., description='The public portion of a customer-generated key pair.'
    )
    tags: Optional[Dict[str, TagValue]] = Field(
        None,
        description='Any tags provided with the request are added to the playback key pair tags. See <a href="https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html">Tagging Amazon Web Services Resources</a> for more information, including restrictions that apply to tags and "Tag naming limits and requirements"; Amazon IVS has no service-specific constraints beyond what is documented there.',
    )


class ListChannelsPostRequest(BaseModel):
    filterByName: Optional[
        constr(pattern=r'^[a-zA-Z0-9-_]*$', min_length=0, max_length=128)
    ] = Field(None, description='Filters the channel list to match the specified name.')
    filterByRecordingConfigurationArn: Optional[
        constr(
            pattern=r'^$|^arn:aws:ivs:[a-z0-9-]+:[0-9]+:recording-configuration/[a-zA-Z0-9-]+$',
            min_length=0,
            max_length=128,
        )
    ] = Field(
        None,
        description='Filters the channel list to match the specified recording-configuration ARN.',
    )
    maxResults: Optional[conint(ge=1, le=100)] = Field(
        None, description='Maximum number of channels to return. Default: 100.'
    )
    nextToken: Optional[
        constr(pattern=r'^[a-zA-Z0-9+/=_-]*$', min_length=0, max_length=1024)
    ] = Field(
        None,
        description='The first channel to retrieve. This is used for pagination; see the <code>nextToken</code> response field.',
    )


class ListPlaybackKeyPairsPostRequest(BaseModel):
    maxResults: Optional[conint(ge=1, le=100)] = Field(
        None,
        description='Maximum number of key pairs to return. Default: your service quota or 100, whichever is smaller.',
    )
    nextToken: Optional[
        constr(pattern=r'^[a-zA-Z0-9+/=_-]*$', min_length=0, max_length=1024)
    ] = Field(
        None,
        description='The first key pair to retrieve. This is used for pagination; see the <code>nextToken</code> response field.',
    )


class ListRecordingConfigurationsPostRequest(BaseModel):
    maxResults: Optional[conint(ge=1, le=100)] = Field(
        None,
        description='Maximum number of recording configurations to return. Default: your service quota or 100, whichever is smaller. ',
    )
    nextToken: Optional[
        constr(pattern=r'^[a-zA-Z0-9+/=_-]*$', min_length=0, max_length=1024)
    ] = Field(
        None,
        description='The first recording configuration to retrieve. This is used for pagination; see the <code>nextToken</code> response field.',
    )


class ListStreamKeysPostRequest(BaseModel):
    channelArn: constr(
        pattern=r'^arn:aws:[is]vs:[a-z0-9-]+:[0-9]+:channel/[a-zA-Z0-9-]+$',
        min_length=1,
        max_length=128,
    ) = Field(..., description='Channel ARN used to filter the list.')
    maxResults: Optional[conint(ge=1, le=50)] = Field(
        None, description='Maximum number of streamKeys to return. Default: 1.'
    )
    nextToken: Optional[
        constr(pattern=r'^[a-zA-Z0-9+/=_-]*$', min_length=0, max_length=1024)
    ] = Field(
        None,
        description='The first stream key to retrieve. This is used for pagination; see the <code>nextToken</code> response field.',
    )


class ListStreamSessionsPostRequest(BaseModel):
    channelArn: constr(
        pattern=r'^arn:aws:[is]vs:[a-z0-9-]+:[0-9]+:channel/[a-zA-Z0-9-]+$',
        min_length=1,
        max_length=128,
    ) = Field(..., description='Channel ARN used to filter the list.')
    maxResults: Optional[conint(ge=1, le=100)] = Field(
        None, description='Maximum number of streams to return. Default: 100.'
    )
    nextToken: Optional[
        constr(pattern=r'^[a-zA-Z0-9+/=_-]*$', min_length=0, max_length=1024)
    ] = Field(
        None,
        description='The first stream to retrieve. This is used for pagination; see the <code>nextToken</code> response field.',
    )


class FilterBy(BaseModel):
    health: Optional[StreamHealth] = None


class ListStreamsPostRequest(BaseModel):
    filterBy: Optional[FilterBy] = Field(
        None, description='Object specifying the stream attribute on which to filter.'
    )
    maxResults: Optional[conint(ge=1, le=100)] = Field(
        None, description='Maximum number of streams to return. Default: 100.'
    )
    nextToken: Optional[
        constr(pattern=r'^[a-zA-Z0-9+/=_-]*$', min_length=0, max_length=1024)
    ] = Field(
        None,
        description='The first stream to retrieve. This is used for pagination; see the <code>nextToken</code> response field.',
    )


class PutMetadataPostRequest(BaseModel):
    channelArn: constr(
        pattern=r'^arn:aws:[is]vs:[a-z0-9-]+:[0-9]+:channel/[a-zA-Z0-9-]+$',
        min_length=1,
        max_length=128,
    ) = Field(
        ...,
        description='ARN of the channel into which metadata is inserted. This channel must have an active stream.',
    )
    metadata: SecretStr = Field(
        ...,
        description='Metadata to insert into the stream. Maximum: 1 KB per request.',
    )


class StopStreamPostRequest(BaseModel):
    channelArn: constr(
        pattern=r'^arn:aws:[is]vs:[a-z0-9-]+:[0-9]+:channel/[a-zA-Z0-9-]+$',
        min_length=1,
        max_length=128,
    ) = Field(
        ..., description='ARN of the channel for which the stream is to be stopped.'
    )


class UpdateChannelPostRequest(BaseModel):
    arn: constr(
        pattern=r'^arn:aws:[is]vs:[a-z0-9-]+:[0-9]+:channel/[a-zA-Z0-9-]+$',
        min_length=1,
        max_length=128,
    ) = Field(..., description='ARN of the channel to be updated.')
    authorized: Optional[bool] = Field(
        None,
        description='Whether the channel is private (enabled for playback authorization).',
    )
    insecureIngest: Optional[bool] = Field(
        None,
        description='Whether the channel allows insecure RTMP ingest. Default: <code>false</code>.',
    )
    latencyMode: Optional[LatencyMode] = Field(
        None,
        description='Channel latency mode. Use <code>NORMAL</code> to broadcast and deliver live video up to Full HD. Use <code>LOW</code> for near-real-time interaction with viewers. (Note: In the Amazon IVS console, <code>LOW</code> and <code>NORMAL</code> correspond to Ultra-low and Standard, respectively.)',
    )
    name: Optional[
        constr(pattern=r'^[a-zA-Z0-9-_]*$', min_length=0, max_length=128)
    ] = Field(None, description='Channel name.')
    recordingConfigurationArn: Optional[
        constr(
            pattern=r'^$|^arn:aws:ivs:[a-z0-9-]+:[0-9]+:recording-configuration/[a-zA-Z0-9-]+$',
            min_length=0,
            max_length=128,
        )
    ] = Field(
        None,
        description='Recording-configuration ARN. If this is set to an empty string, recording is disabled. A value other than an empty string indicates that recording is enabled',
    )
    type: Optional[Type] = Field(
        None,
        description='<p>Channel type, which determines the allowable resolution and bitrate. <i>If you exceed the allowable resolution or bitrate, the stream probably will disconnect immediately</i>. Valid values:</p> <ul> <li> <p> <code>STANDARD</code>: Video is transcoded: multiple qualities are generated from the original input, to automatically give viewers the best experience for their devices and network conditions. Transcoding allows higher playback quality across a range of download speeds. Resolution can be up to 1080p and bitrate can be up to 8.5 Mbps. Audio is transcoded only for renditions 360p and below; above that, audio is passed through. This is the default.</p> </li> <li> <p> <code>BASIC</code>: Video is transmuxed: Amazon IVS delivers the original input to viewers. The viewer’s video-quality choice is limited to the original input. Resolution can be up to 1080p and bitrate can be up to 1.5 Mbps for 480p and up to 3.5 Mbps for resolutions between 480p and 1080p.</p> </li> </ul>',
    )


class TagsResourceArnPostRequest(BaseModel):
    tags: Dict[str, TagValue] = Field(
        ...,
        description='Array of tags to be added or updated. Array of maps, each of the form <code>string:string (key:value)</code>. See <a href="https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html">Tagging Amazon Web Services Resources</a> for more information, including restrictions that apply to tags and "Tag naming limits and requirements"; Amazon IVS has no service-specific constraints beyond what is documented there.',
    )


class TagKeys(RootModel[List[TagKey]]):
    root: List[TagKey] = Field(..., max_length=50, min_length=0)


class AudioConfiguration(BaseModel):
    channels: Optional[Integer] = None
    codec: Optional[String] = None
    sampleRate: Optional[Integer] = None
    targetBitrate: Optional[Integer] = None


class BatchError(BaseModel):
    arn: Optional[ResourceArn] = None
    code: Optional[ErrorCode] = None
    message: Optional[ErrorMessage] = None


class BatchErrors(RootModel[List[BatchError]]):
    root: List[BatchError]


class BatchGetChannelRequest(BaseModel):
    arns: ChannelArnList


class BatchGetStreamKeyRequest(BaseModel):
    arns: StreamKeyArnList


class Channel(BaseModel):
    arn: Optional[ChannelArn] = None
    authorized: Optional[IsAuthorized] = None
    ingestEndpoint: Optional[IngestEndpoint] = None
    insecureIngest: Optional[InsecureIngest] = None
    latencyMode: Optional[ChannelLatencyMode] = None
    name: Optional[ChannelName] = None
    playbackUrl: Optional[PlaybackURL] = None
    recordingConfigurationArn: Optional[ChannelRecordingConfigurationArn] = None
    tags: Optional[Tags] = None
    type: Optional[ChannelType] = None


class ChannelSummary(BaseModel):
    arn: Optional[ChannelArn] = None
    authorized: Optional[IsAuthorized] = None
    insecureIngest: Optional[InsecureIngest] = None
    latencyMode: Optional[ChannelLatencyMode] = None
    name: Optional[ChannelName] = None
    recordingConfigurationArn: Optional[ChannelRecordingConfigurationArn] = None
    tags: Optional[Tags] = None


class Channels(RootModel[List[Channel]]):
    root: List[Channel]


class CreateChannelRequest(BaseModel):
    authorized: Optional[Boolean] = None
    insecureIngest: Optional[Boolean] = None
    latencyMode: Optional[ChannelLatencyMode] = None
    name: Optional[ChannelName] = None
    recordingConfigurationArn: Optional[ChannelRecordingConfigurationArn] = None
    tags: Optional[Tags] = None
    type: Optional[ChannelType] = None


class CreateStreamKeyRequest(BaseModel):
    channelArn: ChannelArn
    tags: Optional[Tags] = None


class DeletePlaybackKeyPairRequest(BaseModel):
    arn: PlaybackKeyPairArn


class DeleteRecordingConfigurationRequest(BaseModel):
    arn: RecordingConfigurationArn


class DeleteStreamKeyRequest(BaseModel):
    arn: StreamKeyArn


class GetChannelResponse(BaseModel):
    channel: Optional[Channel] = None


class GetPlaybackKeyPairRequest(BaseModel):
    arn: PlaybackKeyPairArn


class GetRecordingConfigurationRequest(BaseModel):
    arn: RecordingConfigurationArn


class GetStreamKeyRequest(BaseModel):
    arn: StreamKeyArn


class GetStreamSessionRequest(BaseModel):
    channelArn: ChannelArn
    streamId: Optional[StreamId] = None


class ImportPlaybackKeyPairRequest(BaseModel):
    name: Optional[PlaybackKeyPairName] = None
    publicKeyMaterial: PlaybackPublicKeyMaterial
    tags: Optional[Tags] = None


class IngestConfiguration(BaseModel):
    audio: Optional[AudioConfiguration] = None
    video: Optional[VideoConfiguration] = None


class ListChannelsRequest(BaseModel):
    filterByName: Optional[ChannelName] = None
    filterByRecordingConfigurationArn: Optional[ChannelRecordingConfigurationArn] = None
    maxResults: Optional[MaxChannelResults] = None
    nextToken: Optional[PaginationToken] = None


class ListPlaybackKeyPairsRequest(BaseModel):
    maxResults: Optional[MaxPlaybackKeyPairResults] = None
    nextToken: Optional[PaginationToken] = None


class ListRecordingConfigurationsRequest(BaseModel):
    maxResults: Optional[MaxRecordingConfigurationResults] = None
    nextToken: Optional[PaginationToken] = None


class ListStreamKeysRequest(BaseModel):
    channelArn: ChannelArn
    maxResults: Optional[MaxStreamKeyResults] = None
    nextToken: Optional[PaginationToken] = None


class ListStreamSessionsRequest(BaseModel):
    channelArn: ChannelArn
    maxResults: Optional[MaxStreamResults] = None
    nextToken: Optional[PaginationToken] = None


class ListTagsForResourceResponse(BaseModel):
    tags: Tags


class PlaybackKeyPair(BaseModel):
    arn: Optional[PlaybackKeyPairArn] = None
    fingerprint: Optional[PlaybackKeyPairFingerprint] = None
    name: Optional[PlaybackKeyPairName] = None
    tags: Optional[Tags] = None


class PlaybackKeyPairSummary(BaseModel):
    arn: Optional[PlaybackKeyPairArn] = None
    name: Optional[PlaybackKeyPairName] = None
    tags: Optional[Tags] = None


class PutMetadataRequest(BaseModel):
    channelArn: ChannelArn
    metadata: StreamMetadata


class RecordingConfiguration(BaseModel):
    arn: RecordingConfigurationArn
    destinationConfiguration: DestinationConfiguration
    name: Optional[RecordingConfigurationName] = None
    recordingReconnectWindowSeconds: Optional[RecordingReconnectWindowSeconds] = None
    state: RecordingConfigurationState
    tags: Optional[Tags] = None
    thumbnailConfiguration: Optional[ThumbnailConfiguration] = None


class RecordingConfigurationSummary(BaseModel):
    arn: RecordingConfigurationArn
    destinationConfiguration: DestinationConfiguration
    name: Optional[RecordingConfigurationName] = None
    state: RecordingConfigurationState
    tags: Optional[Tags] = None


class Stream(BaseModel):
    channelArn: Optional[ChannelArn] = None
    health: Optional[StreamHealth] = None
    playbackUrl: Optional[PlaybackURL] = None
    startTime: Optional[StreamStartTime] = None
    state: Optional[StreamState] = None
    streamId: Optional[StreamId] = None
    viewerCount: Optional[StreamViewerCount] = None


class StreamEvent(BaseModel):
    eventTime: Optional[Time] = None
    name: Optional[String] = None
    type: Optional[String] = None


class StreamEvents(RootModel[List[StreamEvent]]):
    root: List[StreamEvent] = Field(..., max_length=500, min_length=0)


class StreamFilters(BaseModel):
    health: Optional[StreamHealth] = None


class StreamKey(BaseModel):
    arn: Optional[StreamKeyArn] = None
    channelArn: Optional[ChannelArn] = None
    tags: Optional[Tags] = None
    value: Optional[StreamKeyValue] = None


class StreamKeySummary(BaseModel):
    arn: Optional[StreamKeyArn] = None
    channelArn: Optional[ChannelArn] = None
    tags: Optional[Tags] = None


class StreamKeys(RootModel[List[StreamKey]]):
    root: List[StreamKey]


class StreamSession(BaseModel):
    channel: Optional[Channel] = None
    endTime: Optional[Time] = None
    ingestConfiguration: Optional[IngestConfiguration] = None
    recordingConfiguration: Optional[RecordingConfiguration] = None
    startTime: Optional[Time] = None
    streamId: Optional[StreamId] = None
    truncatedEvents: Optional[StreamEvents] = None


class StreamSessionSummary(BaseModel):
    endTime: Optional[Time] = None
    hasErrorEvent: Optional[Boolean] = None
    startTime: Optional[Time] = None
    streamId: Optional[StreamId] = None


class StreamSummary(BaseModel):
    channelArn: Optional[ChannelArn] = None
    health: Optional[StreamHealth] = None
    startTime: Optional[StreamStartTime] = None
    state: Optional[StreamState] = None
    streamId: Optional[StreamId] = None
    viewerCount: Optional[StreamViewerCount] = None


class TagResourceRequest(BaseModel):
    tags: Tags


class UpdateChannelResponse(BaseModel):
    channel: Optional[Channel] = None


class BatchGetChannelResponse(BaseModel):
    channels: Optional[Channels] = None
    errors: Optional[BatchErrors] = None


class BatchGetStreamKeyResponse(BaseModel):
    errors: Optional[BatchErrors] = None
    streamKeys: Optional[StreamKeys] = None


class ChannelList(RootModel[List[ChannelSummary]]):
    root: List[ChannelSummary]


class CreateChannelResponse(BaseModel):
    channel: Optional[Channel] = None
    streamKey: Optional[StreamKey] = None


class CreateRecordingConfigurationRequest(BaseModel):
    destinationConfiguration: DestinationConfiguration
    name: Optional[RecordingConfigurationName] = None
    recordingReconnectWindowSeconds: Optional[RecordingReconnectWindowSeconds] = None
    tags: Optional[Tags] = None
    thumbnailConfiguration: Optional[ThumbnailConfiguration] = None


class CreateRecordingConfigurationResponse(BaseModel):
    recordingConfiguration: Optional[RecordingConfiguration] = None


class CreateStreamKeyResponse(BaseModel):
    streamKey: Optional[StreamKey] = None


class GetPlaybackKeyPairResponse(BaseModel):
    keyPair: Optional[PlaybackKeyPair] = None


class GetRecordingConfigurationResponse(BaseModel):
    recordingConfiguration: Optional[RecordingConfiguration] = None


class GetStreamKeyResponse(BaseModel):
    streamKey: Optional[StreamKey] = None


class GetStreamResponse(BaseModel):
    stream: Optional[Stream] = None


class GetStreamSessionResponse(BaseModel):
    streamSession: Optional[StreamSession] = None


class ImportPlaybackKeyPairResponse(BaseModel):
    keyPair: Optional[PlaybackKeyPair] = None


class ListChannelsResponse(BaseModel):
    channels: ChannelList
    nextToken: Optional[PaginationToken] = None


class ListStreamsRequest(BaseModel):
    filterBy: Optional[StreamFilters] = None
    maxResults: Optional[MaxStreamResults] = None
    nextToken: Optional[PaginationToken] = None


class PlaybackKeyPairList(RootModel[List[PlaybackKeyPairSummary]]):
    root: List[PlaybackKeyPairSummary]


class RecordingConfigurationList(RootModel[List[RecordingConfigurationSummary]]):
    root: List[RecordingConfigurationSummary]


class StreamKeyList(RootModel[List[StreamKeySummary]]):
    root: List[StreamKeySummary]


class StreamList(RootModel[List[StreamSummary]]):
    root: List[StreamSummary]


class StreamSessionList(RootModel[List[StreamSessionSummary]]):
    root: List[StreamSessionSummary]


class ListPlaybackKeyPairsResponse(BaseModel):
    keyPairs: PlaybackKeyPairList
    nextToken: Optional[PaginationToken] = None


class ListRecordingConfigurationsResponse(BaseModel):
    nextToken: Optional[PaginationToken] = None
    recordingConfigurations: RecordingConfigurationList


class ListStreamKeysResponse(BaseModel):
    nextToken: Optional[PaginationToken] = None
    streamKeys: StreamKeyList


class ListStreamSessionsResponse(BaseModel):
    nextToken: Optional[PaginationToken] = None
    streamSessions: StreamSessionList


class ListStreamsResponse(BaseModel):
    nextToken: Optional[PaginationToken] = None
    streams: StreamList
