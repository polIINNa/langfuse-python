# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing
from json.decoder import JSONDecodeError

from ...core.api_error import ApiError
from ...core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ...core.datetime_utils import serialize_datetime
from ...core.jsonable_encoder import jsonable_encoder
from ...core.pydantic_utilities import pydantic_v1
from ...core.request_options import RequestOptions
from ..commons.errors.access_denied_error import AccessDeniedError
from ..commons.errors.error import Error
from ..commons.errors.method_not_allowed_error import MethodNotAllowedError
from ..commons.errors.not_found_error import NotFoundError
from ..commons.errors.unauthorized_error import UnauthorizedError
from ..commons.types.trace_with_full_details import TraceWithFullDetails
from .types.traces import Traces


class TraceClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get(
        self, trace_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> TraceWithFullDetails:
        """
        Get a specific trace

        Parameters
        ----------
        trace_id : str
            The unique langfuse identifier of a trace

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TraceWithFullDetails

        Examples
        --------
        from langfuse.client import FernLangfuse

        client = FernLangfuse(
            x_langfuse_sdk_name="YOUR_X_LANGFUSE_SDK_NAME",
            x_langfuse_sdk_version="YOUR_X_LANGFUSE_SDK_VERSION",
            x_langfuse_public_key="YOUR_X_LANGFUSE_PUBLIC_KEY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.trace.get(
            trace_id="string",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/public/traces/{jsonable_encoder(trace_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(TraceWithFullDetails, _response.json())  # type: ignore
            if _response.status_code == 400:
                raise Error(pydantic_v1.parse_obj_as(typing.Any, _response.json()))  # type: ignore
            if _response.status_code == 401:
                raise UnauthorizedError(
                    pydantic_v1.parse_obj_as(typing.Any, _response.json())
                )  # type: ignore
            if _response.status_code == 403:
                raise AccessDeniedError(
                    pydantic_v1.parse_obj_as(typing.Any, _response.json())
                )  # type: ignore
            if _response.status_code == 405:
                raise MethodNotAllowedError(
                    pydantic_v1.parse_obj_as(typing.Any, _response.json())
                )  # type: ignore
            if _response.status_code == 404:
                raise NotFoundError(
                    pydantic_v1.parse_obj_as(typing.Any, _response.json())
                )  # type: ignore
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def list(
        self,
        *,
        page: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        user_id: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        session_id: typing.Optional[str] = None,
        from_timestamp: typing.Optional[dt.datetime] = None,
        to_timestamp: typing.Optional[dt.datetime] = None,
        order_by: typing.Optional[str] = None,
        tags: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        version: typing.Optional[str] = None,
        release: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Traces:
        """
        Get list of traces

        Parameters
        ----------
        page : typing.Optional[int]
            Page number, starts at 1

        limit : typing.Optional[int]
            Limit of items per page. If you encounter api issues due to too large page sizes, try to reduce the limit.

        user_id : typing.Optional[str]

        name : typing.Optional[str]

        session_id : typing.Optional[str]

        from_timestamp : typing.Optional[dt.datetime]
            Optional filter to only include traces with a trace.timestamp on or after a certain datetime (ISO 8601)

        to_timestamp : typing.Optional[dt.datetime]
            Optional filter to only include traces with a trace.timestamp before a certain datetime (ISO 8601)

        order_by : typing.Optional[str]
            Format of the string [field].[asc/desc]. Fields: id, timestamp, name, userId, release, version, public, bookmarked, sessionId. Example: timestamp.asc

        tags : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Only traces that include all of these tags will be returned.

        version : typing.Optional[str]
            Optional filter to only include traces with a certain version.

        release : typing.Optional[str]
            Optional filter to only include traces with a certain release.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Traces

        Examples
        --------
        import datetime

        from langfuse.client import FernLangfuse

        client = FernLangfuse(
            x_langfuse_sdk_name="YOUR_X_LANGFUSE_SDK_NAME",
            x_langfuse_sdk_version="YOUR_X_LANGFUSE_SDK_VERSION",
            x_langfuse_public_key="YOUR_X_LANGFUSE_PUBLIC_KEY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.trace.list(
            page=1,
            limit=1,
            user_id="string",
            name="string",
            session_id="string",
            from_timestamp=datetime.datetime.fromisoformat(
                "2024-01-15 09:30:00+00:00",
            ),
            to_timestamp=datetime.datetime.fromisoformat(
                "2024-01-15 09:30:00+00:00",
            ),
            order_by="string",
            tags="string",
            version="string",
            release="string",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/public/traces",
            method="GET",
            params={
                "page": page,
                "limit": limit,
                "userId": user_id,
                "name": name,
                "sessionId": session_id,
                "fromTimestamp": serialize_datetime(from_timestamp)
                if from_timestamp is not None
                else None,
                "toTimestamp": serialize_datetime(to_timestamp)
                if to_timestamp is not None
                else None,
                "orderBy": order_by,
                "tags": tags,
                "version": version,
                "release": release,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(Traces, _response.json())  # type: ignore
            if _response.status_code == 400:
                raise Error(pydantic_v1.parse_obj_as(typing.Any, _response.json()))  # type: ignore
            if _response.status_code == 401:
                raise UnauthorizedError(
                    pydantic_v1.parse_obj_as(typing.Any, _response.json())
                )  # type: ignore
            if _response.status_code == 403:
                raise AccessDeniedError(
                    pydantic_v1.parse_obj_as(typing.Any, _response.json())
                )  # type: ignore
            if _response.status_code == 405:
                raise MethodNotAllowedError(
                    pydantic_v1.parse_obj_as(typing.Any, _response.json())
                )  # type: ignore
            if _response.status_code == 404:
                raise NotFoundError(
                    pydantic_v1.parse_obj_as(typing.Any, _response.json())
                )  # type: ignore
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncTraceClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get(
        self, trace_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> TraceWithFullDetails:
        """
        Get a specific trace

        Parameters
        ----------
        trace_id : str
            The unique langfuse identifier of a trace

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TraceWithFullDetails

        Examples
        --------
        import asyncio

        from langfuse.client import AsyncFernLangfuse

        client = AsyncFernLangfuse(
            x_langfuse_sdk_name="YOUR_X_LANGFUSE_SDK_NAME",
            x_langfuse_sdk_version="YOUR_X_LANGFUSE_SDK_VERSION",
            x_langfuse_public_key="YOUR_X_LANGFUSE_PUBLIC_KEY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.trace.get(
                trace_id="string",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/public/traces/{jsonable_encoder(trace_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(TraceWithFullDetails, _response.json())  # type: ignore
            if _response.status_code == 400:
                raise Error(pydantic_v1.parse_obj_as(typing.Any, _response.json()))  # type: ignore
            if _response.status_code == 401:
                raise UnauthorizedError(
                    pydantic_v1.parse_obj_as(typing.Any, _response.json())
                )  # type: ignore
            if _response.status_code == 403:
                raise AccessDeniedError(
                    pydantic_v1.parse_obj_as(typing.Any, _response.json())
                )  # type: ignore
            if _response.status_code == 405:
                raise MethodNotAllowedError(
                    pydantic_v1.parse_obj_as(typing.Any, _response.json())
                )  # type: ignore
            if _response.status_code == 404:
                raise NotFoundError(
                    pydantic_v1.parse_obj_as(typing.Any, _response.json())
                )  # type: ignore
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def list(
        self,
        *,
        page: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        user_id: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        session_id: typing.Optional[str] = None,
        from_timestamp: typing.Optional[dt.datetime] = None,
        to_timestamp: typing.Optional[dt.datetime] = None,
        order_by: typing.Optional[str] = None,
        tags: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        version: typing.Optional[str] = None,
        release: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Traces:
        """
        Get list of traces

        Parameters
        ----------
        page : typing.Optional[int]
            Page number, starts at 1

        limit : typing.Optional[int]
            Limit of items per page. If you encounter api issues due to too large page sizes, try to reduce the limit.

        user_id : typing.Optional[str]

        name : typing.Optional[str]

        session_id : typing.Optional[str]

        from_timestamp : typing.Optional[dt.datetime]
            Optional filter to only include traces with a trace.timestamp on or after a certain datetime (ISO 8601)

        to_timestamp : typing.Optional[dt.datetime]
            Optional filter to only include traces with a trace.timestamp before a certain datetime (ISO 8601)

        order_by : typing.Optional[str]
            Format of the string [field].[asc/desc]. Fields: id, timestamp, name, userId, release, version, public, bookmarked, sessionId. Example: timestamp.asc

        tags : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Only traces that include all of these tags will be returned.

        version : typing.Optional[str]
            Optional filter to only include traces with a certain version.

        release : typing.Optional[str]
            Optional filter to only include traces with a certain release.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Traces

        Examples
        --------
        import asyncio
        import datetime

        from langfuse.client import AsyncFernLangfuse

        client = AsyncFernLangfuse(
            x_langfuse_sdk_name="YOUR_X_LANGFUSE_SDK_NAME",
            x_langfuse_sdk_version="YOUR_X_LANGFUSE_SDK_VERSION",
            x_langfuse_public_key="YOUR_X_LANGFUSE_PUBLIC_KEY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.trace.list(
                page=1,
                limit=1,
                user_id="string",
                name="string",
                session_id="string",
                from_timestamp=datetime.datetime.fromisoformat(
                    "2024-01-15 09:30:00+00:00",
                ),
                to_timestamp=datetime.datetime.fromisoformat(
                    "2024-01-15 09:30:00+00:00",
                ),
                order_by="string",
                tags="string",
                version="string",
                release="string",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/public/traces",
            method="GET",
            params={
                "page": page,
                "limit": limit,
                "userId": user_id,
                "name": name,
                "sessionId": session_id,
                "fromTimestamp": serialize_datetime(from_timestamp)
                if from_timestamp is not None
                else None,
                "toTimestamp": serialize_datetime(to_timestamp)
                if to_timestamp is not None
                else None,
                "orderBy": order_by,
                "tags": tags,
                "version": version,
                "release": release,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(Traces, _response.json())  # type: ignore
            if _response.status_code == 400:
                raise Error(pydantic_v1.parse_obj_as(typing.Any, _response.json()))  # type: ignore
            if _response.status_code == 401:
                raise UnauthorizedError(
                    pydantic_v1.parse_obj_as(typing.Any, _response.json())
                )  # type: ignore
            if _response.status_code == 403:
                raise AccessDeniedError(
                    pydantic_v1.parse_obj_as(typing.Any, _response.json())
                )  # type: ignore
            if _response.status_code == 405:
                raise MethodNotAllowedError(
                    pydantic_v1.parse_obj_as(typing.Any, _response.json())
                )  # type: ignore
            if _response.status_code == 404:
                raise NotFoundError(
                    pydantic_v1.parse_obj_as(typing.Any, _response.json())
                )  # type: ignore
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
