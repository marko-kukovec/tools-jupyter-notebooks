# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: stratum_rpc.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x11stratum_rpc.proto\"5\n\x12RpcStatPingRequest\x12\x0c\n\x04\x61lgo\x18\x01 \x01(\x05\x12\x11\n\ttimestamp\x18\x02 \x01(\x03\"~\n\x13RpcStatPingResponse\x12\x0c\n\x04\x61lgo\x18\x01 \x01(\x05\x12\x19\n\x11receive_timestamp\x18\x02 \x01(\x03\x12\x1a\n\x12response_timestamp\x18\x03 \x01(\x03\x12\"\n\x06status\x18\x04 \x01(\x0b\x32\x12.RpcResponseStatus\"\xcd\x01\n\x15RpcOrderCreateRequest\x12\r\n\x05order\x18\x01 \x01(\t\x12\x0c\n\x04\x61lgo\x18\x02 \x01(\x05\x12\x0e\n\x06\x61mount\x18\x03 \x01(\x03\x12\r\n\x05price\x18\x04 \x01(\x01\x12\r\n\x05limit\x18\x05 \x01(\x01\x12\x1b\n\x04type\x18\x06 \x01(\x0e\x32\r.RpcOrderType\x12\x10\n\x08poolHost\x18\x07 \x01(\t\x12\x10\n\x08poolPort\x18\x08 \x01(\x05\x12\x10\n\x08poolUser\x18\t \x01(\t\x12\x10\n\x08poolPass\x18\n \x01(\tJ\x04\x08\x0b\x10\x0c\"Y\n\x16RpcOrderCreateResponse\x12\r\n\x05order\x18\x01 \x01(\t\x12\x0c\n\x04\x61lgo\x18\x02 \x01(\x05\x12\"\n\x06status\x18\x03 \x01(\x0b\x32\x12.RpcResponseStatus\"D\n\x15RpcOrderCancelRequest\x12\r\n\x05order\x18\x01 \x01(\t\x12\x0c\n\x04\x61lgo\x18\x02 \x01(\x05\x12\x0e\n\x06reason\x18\x03 \x01(\t\"Y\n\x16RpcOrderCancelResponse\x12\r\n\x05order\x18\x01 \x01(\t\x12\x0c\n\x04\x61lgo\x18\x02 \x01(\x05\x12\"\n\x06status\x18\x03 \x01(\x0b\x32\x12.RpcResponseStatus\"D\n\x15RpcOrderRefillRequest\x12\r\n\x05order\x18\x01 \x01(\t\x12\x0c\n\x04\x61lgo\x18\x02 \x01(\x05\x12\x0e\n\x06\x61mount\x18\x03 \x01(\x03\"Y\n\x16RpcOrderRefillResponse\x12\r\n\x05order\x18\x01 \x01(\t\x12\x0c\n\x04\x61lgo\x18\x02 \x01(\x05\x12\"\n\x06status\x18\x03 \x01(\x0b\x32\x12.RpcResponseStatus\"G\n\x18RpcOrderSetAmountRequest\x12\r\n\x05order\x18\x01 \x01(\t\x12\x0c\n\x04\x61lgo\x18\x02 \x01(\x05\x12\x0e\n\x06\x61mount\x18\x03 \x01(\x03\"\\\n\x19RpcOrderSetAmountResponse\x12\r\n\x05order\x18\x01 \x01(\t\x12\x0c\n\x04\x61lgo\x18\x02 \x01(\x05\x12\"\n\x06status\x18\x03 \x01(\x0b\x32\x12.RpcResponseStatus\"K\n\x17RpcOrderSetLimitRequest\x12\r\n\x05order\x18\x01 \x01(\t\x12\x0c\n\x04\x61lgo\x18\x02 \x01(\x05\x12\r\n\x05limit\x18\x03 \x01(\x01J\x04\x08\x04\x10\x05\"[\n\x18RpcOrderSetLimitResponse\x12\r\n\x05order\x18\x01 \x01(\t\x12\x0c\n\x04\x61lgo\x18\x02 \x01(\x05\x12\"\n\x06status\x18\x03 \x01(\x0b\x32\x12.RpcResponseStatus\"K\n\x17RpcOrderSetPriceRequest\x12\r\n\x05order\x18\x01 \x01(\t\x12\x0c\n\x04\x61lgo\x18\x02 \x01(\x05\x12\r\n\x05price\x18\x03 \x01(\x01J\x04\x08\x04\x10\x05\"[\n\x18RpcOrderSetPriceResponse\x12\r\n\x05order\x18\x01 \x01(\t\x12\x0c\n\x04\x61lgo\x18\x02 \x01(\x05\x12\"\n\x06status\x18\x03 \x01(\x0b\x32\x12.RpcResponseStatus\"r\n\x15RpcOrderUpdateRequest\x12\r\n\x05order\x18\x01 \x01(\t\x12\x0c\n\x04\x61lgo\x18\x02 \x01(\x05\x12\x0e\n\x06\x61mount\x18\x03 \x01(\x03\x12\x0e\n\x06refill\x18\x04 \x01(\x03\x12\r\n\x05price\x18\x05 \x01(\x01\x12\r\n\x05limit\x18\x06 \x01(\x01\"Y\n\x16RpcOrderUpdateResponse\x12\r\n\x05order\x18\x01 \x01(\t\x12\x0c\n\x04\x61lgo\x18\x02 \x01(\x05\x12\"\n\x06status\x18\x03 \x01(\x0b\x32\x12.RpcResponseStatus\"\x1e\n\x0bRpcResponse\x12\x0f\n\x07message\x18\x01 \x01(\t\"\x87\x01\n\rRpcRigRequest\x12\x11\n\trequestId\x18\x01 \x01(\t\x12\x11\n\tstratumId\x18\x02 \x01(\t\x12\x17\n\x0fintervalEndTime\x18\x03 \x01(\x03\x12\x0c\n\x04\x61lgo\x18\x04 \x01(\x05\x12\x0e\n\x06market\x18\x05 \x01(\x05\x12\x19\n\x04rigs\x18\x06 \x03(\x0b\x32\x0b.RpcRigData\"z\n\nRpcRigData\x12\x12\n\nbtcAddress\x18\x01 \x01(\t\x12\x10\n\x08workerId\x18\x02 \x01(\t\x12\r\n\x05rigId\x18\x03 \x01(\t\x12\x12\n\namountPaid\x18\x04 \x01(\x03\x12#\n\x07summary\x18\x05 \x01(\x0b\x32\x12.RpcRigSummaryData\"\xd4\x02\n\x11RpcRigSummaryData\x12\x12\n\ndifficulty\x18\x01 \x01(\x01\x12\x15\n\rspeedAccepted\x18\x02 \x01(\x01\x12\x1a\n\x12speedRejectedTotal\x18\x03 \x01(\x01\x12\x1d\n\x15speedRejectedR1Target\x18\x04 \x01(\x01\x12\x1c\n\x14speedRejectedR2Stale\x18\x05 \x01(\x01\x12 \n\x18speedRejectedR3Duplicate\x18\x06 \x01(\x01\x12\x1c\n\x14speedRejectedR4NTime\x18\x07 \x01(\x01\x12\x1c\n\x14speedRejectedR5Other\x18\x08 \x01(\x01\x12\x0f\n\x07proxyId\x18\t \x01(\x05\x12\r\n\x05xnsub\x18\n \x01(\x08\x12\x15\n\rtimeConnected\x18\x0b \x01(\x03\x12\x11\n\tipAddress\x18\x0c \x01(\t\x12\r\n\x05miner\x18\r \x01(\tJ\x04\x08\x0e\x10\x15\"\x8d\x01\n\x0fRpcOrderRequest\x12\x11\n\trequestId\x18\x01 \x01(\t\x12\x11\n\tstratumId\x18\x02 \x01(\t\x12\x17\n\x0fintervalEndTime\x18\x03 \x01(\x03\x12\x0c\n\x04\x61lgo\x18\x04 \x01(\x05\x12\x0e\n\x06market\x18\x05 \x01(\x05\x12\x1d\n\x06orders\x18\x06 \x03(\x0b\x32\r.RpcOrderData\"\x9c\x01\n\x0cRpcOrderData\x12\r\n\x05order\x18\x01 \x01(\t\x12#\n\x06\x61mount\x18\x02 \x01(\x0b\x32\x13.RpcOrderAmountData\x12%\n\x07summary\x18\x03 \x01(\x0b\x32\x14.RpcOrderSummaryData\x12\x31\n\x10poolBlockRewards\x18\x04 \x03(\x0b\x32\x17.RpcPoolBlockRewardData\"x\n\x12RpcOrderAmountData\x12\x13\n\x0b\x61mountTotal\x18\x01 \x01(\x03\x12\x12\n\namountPaid\x18\x02 \x01(\x03\x12\x39\n\x10\x63ompletionReason\x18\x03 \x01(\x0e\x32\x1f.RpcOrderAmountCompletionReason\"\xec\x02\n\x13RpcOrderSummaryData\x12\x10\n\x08poolHost\x18\x01 \x01(\t\x12\x10\n\x08poolPort\x18\x02 \x01(\x05\x12\x10\n\x08poolUser\x18\x03 \x01(\t\x12\x10\n\x08poolPass\x18\x04 \x01(\t\x12\x0f\n\x07isAlive\x18\x05 \x01(\x08\x12\r\n\x05limit\x18\x06 \x01(\x01\x12\x10\n\x08refilled\x18\x07 \x01(\x03\x12\x1b\n\x04type\x18\x08 \x01(\x0e\x32\r.RpcOrderType\x12\x1e\n\x08poolStat\x18\t \x01(\x0b\x32\x0c.RpcPoolStat\x12\x1f\n\x07\x62ridges\x18\n \x03(\x0b\x32\x0e.RpcBridgeData\x12*\n\x0e\x62ridgesDataSum\x18\x0e \x01(\x0b\x32\x12.RpcBridgesDataSum\x12\r\n\x05price\x18\x0b \x01(\x01\x12#\n\x1blast_price_change_timestamp\x18\x0c \x01(\x03\x12\x1d\n\x15order_sequence_number\x18\r \x01(\x03\"\x92\x05\n\x0bRpcPoolStat\x12\x15\n\rspeedAccepted\x18\x01 \x01(\x01\x12\x1a\n\x12speedRejectedTotal\x18\x02 \x01(\x01\x12\x1d\n\x15speedRejectedR1Target\x18\x03 \x01(\x01\x12\x1c\n\x14speedRejectedR2Stale\x18\x04 \x01(\x01\x12 \n\x18speedRejectedR3Duplicate\x18\x05 \x01(\x01\x12\x1c\n\x14speedRejectedR4NTime\x18\x06 \x01(\x01\x12\x1c\n\x14speedRejectedR5Other\x18\x07 \x01(\x01\x12\x1d\n\x15speedRejectedR6Worker\x18\x08 \x01(\x01\x12\x1e\n\x16speedRejectedR7Timeout\x18\t \x01(\x01\x12\x16\n\x0esharesAccepted\x18\n \x01(\x05\x12\x1b\n\x13sharesRejectedTotal\x18\x0b \x01(\x05\x12\x1e\n\x16sharesRejectedR1Target\x18\x0c \x01(\x05\x12\x1d\n\x15sharesRejectedR2Stale\x18\r \x01(\x05\x12!\n\x19sharesRejectedR3Duplicate\x18\x0e \x01(\x05\x12\x1d\n\x15sharesRejectedR4NTime\x18\x0f \x01(\x05\x12\x1d\n\x15sharesRejectedR5Other\x18\x10 \x01(\x05\x12\x1e\n\x16sharesRejectedR6Worker\x18\x11 \x01(\x05\x12\x1f\n\x17sharesRejectedR7Timeout\x18\x12 \x01(\x05\x12\x15\n\rsharesMaxDiff\x18\x13 \x01(\x01\x12\x15\n\rglobalMaxDiff\x18\x14 \x01(\x01\x12\x32\n\x0eglobalMaxDiffs\x18\x15 \x03(\x0b\x32\x1a.RpcPoolGlobalDifficulties\"\xe6\x01\n\rRpcBridgeData\x12\x11\n\trigsCount\x18\x01 \x01(\x05\x12\x11\n\tjobsCount\x18\x02 \x01(\x05\x12\x12\n\ndifficulty\x18\x03 \x01(\x01\x12\x15\n\rspeedAccepted\x18\x04 \x01(\x01\x12\x15\n\rspeedRewarded\x18\x05 \x01(\x01\x12\x0e\n\x06status\x18\x06 \x01(\t\x12\x15\n\rspeedRejected\x18\x07 \x01(\x01\x12\x16\n\x0esharesAccepted\x18\x08 \x01(\x05\x12\x16\n\x0esharesRewarded\x18\t \x01(\x05\x12\x16\n\x0esharesRejected\x18\n \x01(\x05\"\xa0\x01\n\x11RpcBridgesDataSum\x12\x15\n\rspeedAccepted\x18\x01 \x01(\x01\x12\x15\n\rspeedRewarded\x18\x02 \x01(\x01\x12\x15\n\rspeedRejected\x18\x03 \x01(\x01\x12\x16\n\x0esharesAccepted\x18\x04 \x01(\x05\x12\x16\n\x0esharesRewarded\x18\x05 \x01(\x05\x12\x16\n\x0esharesRejected\x18\x06 \x01(\x05\"\xd0\x01\n\x16RpcPoolBlockRewardData\x12\x0c\n\x04\x63oin\x18\x01 \x01(\t\x12\x13\n\x0b\x62lockHeight\x18\x02 \x01(\x03\x12\x11\n\tblockHash\x18\x03 \x01(\t\x12\x15\n\rpayoutAddress\x18\x04 \x01(\t\x12\x14\n\x0cpayoutReward\x18\x05 \x01(\x03\x12\x12\n\nfeeAddress\x18\x06 \x01(\t\x12\x11\n\tfeeReward\x18\x07 \x01(\x03\x12\x0c\n\x04time\x18\x08 \x01(\x03\x12\x0c\n\x04txid\x18\t \x01(\t\x12\x10\n\x08isOrphan\x18\n \x01(\x08\"D\n\x19RpcPoolGlobalDifficulties\x12\x0c\n\x04\x63oin\x18\x01 \x01(\t\x12\x19\n\x11networkDifficulty\x18\x02 \x01(\x01\"h\n\x1dRpcStratumStatsSummaryRequest\x12\x11\n\trequestId\x18\x01 \x01(\t\x12\x0c\n\x04\x61lgo\x18\x02 \x01(\x05\x12\r\n\x05price\x18\x03 \x01(\x01\x12\x17\n\x0fintervalEndTime\x18\x04 \x01(\x03\"%\n\x15RpcSpeedAmountRequest\x12\x0c\n\x04\x61lgo\x18\x01 \x01(\x05\"\xa1\x04\n\x16RpcSpeedAmountResponse\x12\x0c\n\x04\x61lgo\x18\x01 \x01(\x05\x12\r\n\x05speed\x18\x02 \x01(\x01\x12\x0e\n\x06\x61mount\x18\x03 \x01(\x03\x12\x17\n\x0flastRoundAmount\x18\x04 \x01(\x03\x12\x15\n\rlastRoundPaid\x18\x05 \x01(\x03\x12\x15\n\rstandardSpeed\x18\x06 \x01(\x01\x12\x12\n\nfixedSpeed\x18\x07 \x01(\x01\x12\x12\n\norderPrice\x18\x08 \x01(\x01\x12\"\n\x06status\x18\t \x01(\x0b\x32\x12.RpcResponseStatus\x12\x1a\n\x12\x66ixedOrderMinPrice\x18\n \x01(\x01\x12\x1a\n\x12\x66ixedOrderMaxPrice\x18\x0b \x01(\x01\x12\x1a\n\x12\x66ixedOrderAvgPrice\x18\x0c \x01(\x01\x12\x1a\n\x12\x66ixedOrderRigCount\x18\r \x01(\x05\x12\x17\n\x0f\x66ixedOrderCount\x18\x0e \x01(\x05\x12\x1d\n\x15standardOrderMinPrice\x18\x0f \x01(\x01\x12\x1d\n\x15standardOrderMaxPrice\x18\x10 \x01(\x01\x12\x1d\n\x15standardOrderAvgPrice\x18\x11 \x01(\x01\x12\x1d\n\x15standardOrderRigCount\x18\x12 \x01(\x05\x12\x1a\n\x12standardOrderCount\x18\x13 \x01(\x05\x12\x0e\n\x06market\x18\x14 \x01(\x05\x12\x16\n\x0e\x64\x65\x61\x64OrderCount\x18\x15 \x01(\x05\"1\n\x12RpcSetPriceRequest\x12\x0c\n\x04\x61lgo\x18\x01 \x01(\x05\x12\r\n\x05price\x18\x02 \x01(\x01\"G\n\x13RpcSetPriceResponse\x12\x0c\n\x04\x61lgo\x18\x01 \x01(\x05\x12\"\n\x06status\x18\x02 \x01(\x0b\x32\x12.RpcResponseStatus\"]\n\x11RpcResponseStatus\x12&\n\x06status\x18\x01 \x01(\x0e\x32\x16.RpcResponseStatusCode\x12 \n\x05\x65rror\x18\x02 \x01(\x0b\x32\x11.RpcResponseError\"1\n\x10RpcResponseError\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x0f\n\x07message\x18\x02 \x01(\t\"/\n\x1aRpcStratumWhiteListRequest\x12\x11\n\tstratumId\x18\x01 \x01(\t\"d\n\x1bRpcStratumWhiteListResponse\x12\x12\n\nip_address\x18\x02 \x03(\t\x12\x13\n\x0b\x62tc_address\x18\x03 \x03(\t\x12\x1c\n\x06status\x18\x04 \x01(\x0b\x32\x0c.RpcResponse\"H\n\x1dRpcStratumWhiteListAddRequest\x12\x12\n\nip_address\x18\x01 \x03(\t\x12\x13\n\x0b\x62tc_address\x18\x02 \x03(\t\"D\n\x1eRpcStratumWhiteListAddResponse\x12\"\n\x06status\x18\x01 \x01(\x0b\x32\x12.RpcResponseStatus\"K\n RpcStratumWhiteListRemoveRequest\x12\x12\n\nip_address\x18\x01 \x03(\t\x12\x13\n\x0b\x62tc_address\x18\x02 \x03(\t\"G\n!RpcStratumWhiteListRemoveResponse\x12\"\n\x06status\x18\x01 \x01(\x0b\x32\x12.RpcResponseStatus\"G\n\x11RpcBlackListEntry\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\t\x12\x0e\n\x06reason\x18\x02 \x01(\t\x12\x11\n\ttimestamp\x18\x03 \x01(\x03\"~\n\x1aRpcStratumBlackListRequest\x12\x11\n\tstratumId\x18\x01 \x01(\t\x12\x1e\n\x02ip\x18\x02 \x03(\x0b\x32\x12.RpcBlackListEntry\x12\x1f\n\x03\x62tc\x18\x03 \x03(\x0b\x32\x12.RpcBlackListEntry\x12\x0c\n\x04\x61lgo\x18\x04 \x01(\x05\"Y\n RpcStratumBlackListRemoveRequest\x12\x0c\n\x04\x61lgo\x18\x01 \x01(\x05\x12\x12\n\nip_address\x18\x02 \x01(\t\x12\x13\n\x0b\x62tc_address\x18\x03 \x01(\t\"G\n!RpcStratumBlackListRemoveResponse\x12\"\n\x06status\x18\x01 \x01(\x0b\x32\x12.RpcResponseStatus\"/\n\x1fRpcStratumBlackListClearRequest\x12\x0c\n\x04\x61lgo\x18\x01 \x01(\x05\"F\n RpcStratumBlackListClearResponse\x12\"\n\x06status\x18\x01 \x01(\x0b\x32\x12.RpcResponseStatus\"\xae\x01\n\x1aRpcStratumAlgoBridgeConfig\x12\x10\n\x08min_diff\x18\x01 \x01(\x01\x12\x14\n\x0c\x62reach_speed\x18\x02 \x01(\x01\x12\x1d\n\x15\x62reach_speed_min_diff\x18\x03 \x01(\x01\x12\x15\n\rfast_job_time\x18\x04 \x01(\x05\x12\x19\n\x11reward_disconnect\x18\x05 \x01(\x01\x12\x17\n\x0freward_fast_job\x18\x06 \x01(\x01\"\x9d\x01\n\x17RpcStratumAlgoRigConfig\x12\x1a\n\x12\x64\x65\x66\x61ult_share_diff\x18\x01 \x01(\x01\x12\x16\n\x0emin_share_diff\x18\x02 \x01(\x01\x12\x16\n\x0emax_share_diff\x18\x03 \x01(\x01\x12\x1a\n\x12vardiff_min_shares\x18\x04 \x01(\x05\x12\x1a\n\x12vardiff_max_shares\x18\x05 \x01(\x05\":\n\x1eRpcStratumAlgoValidatorAddress\x12\n\n\x02ip\x18\x01 \x01(\t\x12\x0c\n\x04port\x18\x02 \x01(\x05\"\xe1\x01\n\x14RpcStratumAlgoConfig\x12\x1b\n\x13max_rigs_per_bridge\x18\x01 \x01(\x05\x12\x11\n\trig_speed\x18\x02 \x01(\x01\x12\x11\n\tmax_kills\x18\x03 \x01(\x05\x12+\n\x06\x62ridge\x18\x04 \x01(\x0b\x32\x1b.RpcStratumAlgoBridgeConfig\x12%\n\x03rig\x18\x05 \x01(\x0b\x32\x18.RpcStratumAlgoRigConfig\x12\x32\n\tvalidator\x18\x06 \x03(\x0b\x32\x1f.RpcStratumAlgoValidatorAddress\"A\n\x1eRpcStratumAlgoConfigGetRequest\x12\x11\n\tstratumId\x18\x01 \x01(\t\x12\x0c\n\x04\x61lgo\x18\x02 \x01(\x05\"f\n\x1fRpcStratumAlgoConfigGetResponse\x12%\n\x06\x63onfig\x18\x01 \x01(\x0b\x32\x15.RpcStratumAlgoConfig\x12\x1c\n\x06status\x18\x02 \x01(\x0b\x32\x0c.RpcResponse\"U\n\x1eRpcStratumAlgoConfigSetRequest\x12\x0c\n\x04\x61lgo\x18\x01 \x01(\x05\x12%\n\x06\x63onfig\x18\x02 \x01(\x0b\x32\x15.RpcStratumAlgoConfig\"E\n\x1fRpcStratumAlgoConfigSetResponse\x12\"\n\x06status\x18\x01 \x01(\x0b\x32\x12.RpcResponseStatus\"E\n\x1bRpcMonitoringAlgorithmStats\x12\x13\n\x0border_count\x18\x01 \x01(\x05\x12\x11\n\trig_count\x18\x02 \x01(\x05\"\x9b\x03\n\x18RpcMonitoringOrdersStats\x12\x17\n\x0fjobs_per_second\x18\x01 \x01(\x01\x12\x14\n\x0c\x62ridge_count\x18\x02 \x01(\x05\x12\"\n\x1a\x61\x63\x63\x65pted_shares_per_second\x18\x03 \x01(\x01\x12)\n!rejected_shares_per_second_target\x18\x04 \x01(\x01\x12(\n rejected_shares_per_second_stale\x18\x05 \x01(\x01\x12,\n$rejected_shares_per_second_duplicate\x18\x06 \x01(\x01\x12(\n rejected_shares_per_second_ntime\x18\x07 \x01(\x01\x12(\n rejected_shares_per_second_other\x18\x08 \x01(\x01\x12)\n!rejected_shares_per_second_worker\x18\t \x01(\x01\x12*\n\"rejected_shares_per_second_timeout\x18\n \x01(\x01\"\xc7\x03\n\x16RpcMonitoringRigsStats\x12\x19\n\x11shares_per_second\x18\x01 \x01(\x01\x12\"\n\x1a\x61\x63\x63\x65pted_shares_per_second\x18\x02 \x01(\x01\x12\"\n\x1arejected_shares_per_second\x18\x03 \x01(\x01\x12\r\n\x05speed\x18\x04 \x01(\x01\x12\x16\n\x0e\x61\x63\x63\x65pted_speed\x18\x05 \x01(\x01\x12\x16\n\x0erejected_speed\x18\x06 \x01(\x01\x12\x10\n\x08min_diff\x18\x07 \x01(\x01\x12\x10\n\x08\x61vg_diff\x18\x08 \x01(\x01\x12\x10\n\x08max_diff\x18\t \x01(\x01\x12)\n!rejected_shares_per_second_target\x18\n \x01(\x01\x12(\n rejected_shares_per_second_stale\x18\x0b \x01(\x01\x12,\n$rejected_shares_per_second_duplicate\x18\x0c \x01(\x01\x12(\n rejected_shares_per_second_ntime\x18\r \x01(\x01\x12(\n rejected_shares_per_second_other\x18\x0e \x01(\x01\"\xa9\x01\n\x1cRpcMonitoringValidatorsStats\x12\x10\n\x08timeouts\x18\x01 \x01(\x05\x12!\n\x19min_response_milliseconds\x18\x02 \x01(\x01\x12!\n\x19\x61vg_response_milliseconds\x18\x03 \x01(\x01\x12!\n\x19max_response_milliseconds\x18\x04 \x01(\x01\x12\x0e\n\x06\x65rrors\x18\x05 \x01(\x05\"u\n\x16RpcMonitoringPushStats\x12\x1d\n\x15min_push_milliseconds\x18\x01 \x01(\x01\x12\x1d\n\x15\x61vg_push_milliseconds\x18\x02 \x01(\x01\x12\x1d\n\x15max_push_milliseconds\x18\x03 \x01(\x01\"\xbb\x02\n\x1dRpcMonitoringAlgorithmRequest\x12\x11\n\tstratumId\x18\x01 \x01(\t\x12\x0c\n\x04\x61lgo\x18\x02 \x01(\x05\x12\x35\n\x0f\x61lgorithm_stats\x18\x03 \x01(\x0b\x32\x1c.RpcMonitoringAlgorithmStats\x12/\n\x0corders_stats\x18\x04 \x01(\x0b\x32\x19.RpcMonitoringOrdersStats\x12+\n\nrigs_stats\x18\x05 \x01(\x0b\x32\x17.RpcMonitoringRigsStats\x12\x37\n\x10validators_stats\x18\x06 \x01(\x0b\x32\x1d.RpcMonitoringValidatorsStats\x12+\n\npush_stats\x18\x07 \x01(\x0b\x32\x17.RpcMonitoringPushStats\"Z\n\x13RpcMonitoringStrand\x12\r\n\x05\x63ount\x18\x01 \x01(\x05\x12\x11\n\tavg_count\x18\x02 \x01(\x05\x12\x11\n\tmax_count\x18\x03 \x01(\x05\x12\x0e\n\x06origin\x18\x04 \x01(\t\"f\n\x1bRpcMonitoringStratumRequest\x12\x11\n\tstratumId\x18\x01 \x01(\t\x12\x0e\n\x06uptime\x18\x02 \x01(\x05\x12$\n\x06strand\x18\x03 \x03(\x0b\x32\x14.RpcMonitoringStrand\"\x8d\x01\n\x11RigOrderStatistic\x12\x11\n\trequestId\x18\x01 \x01(\t\x12\x11\n\tstratumId\x18\x02 \x01(\t\x12\x17\n\x0fintervalEndTime\x18\x03 \x01(\x03\x12\x0c\n\x04\x61lgo\x18\x04 \x01(\x05\x12\x0e\n\x06market\x18\x05 \x01(\x05\x12\x1b\n\x04rigs\x18\x06 \x03(\x0b\x32\r.RigOrderData\"x\n\x0cRigOrderData\x12\x0f\n\x07orderId\x18\x01 \x01(\t\x12\x12\n\nbtcAddress\x18\x02 \x01(\t\x12\x10\n\x08workerId\x18\x03 \x01(\t\x12\r\n\x05rigId\x18\x04 \x01(\t\x12\x0f\n\x07minerId\x18\x05 \x01(\t\x12\x11\n\tipAddress\x18\x06 \x01(\t*>\n\x15RpcResponseStatusCode\x12\x0b\n\x07unknown\x10\x00\x12\x0b\n\x07success\x10\x01\x12\x0b\n\x07\x66\x61ilure\x10\x02*\'\n\x0cRpcOrderType\x12\x0c\n\x08standard\x10\x00\x12\t\n\x05\x66ixed\x10\x01*r\n\x1eRpcOrderAmountCompletionReason\x12\x1b\n\x17unknowncompletionReason\x10\x00\x12\r\n\tcancelled\x10\x01\x12\x0b\n\x07\x65xpired\x10\x02\x12\r\n\tcompleted\x10\x03\x12\x08\n\x04\x64\x65\x61\x64\x10\x04\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'stratum_rpc_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _RPCRESPONSESTATUSCODE._serialized_start=9168
  _RPCRESPONSESTATUSCODE._serialized_end=9230
  _RPCORDERTYPE._serialized_start=9232
  _RPCORDERTYPE._serialized_end=9271
  _RPCORDERAMOUNTCOMPLETIONREASON._serialized_start=9273
  _RPCORDERAMOUNTCOMPLETIONREASON._serialized_end=9387
  _RPCSTATPINGREQUEST._serialized_start=21
  _RPCSTATPINGREQUEST._serialized_end=74
  _RPCSTATPINGRESPONSE._serialized_start=76
  _RPCSTATPINGRESPONSE._serialized_end=202
  _RPCORDERCREATEREQUEST._serialized_start=205
  _RPCORDERCREATEREQUEST._serialized_end=410
  _RPCORDERCREATERESPONSE._serialized_start=412
  _RPCORDERCREATERESPONSE._serialized_end=501
  _RPCORDERCANCELREQUEST._serialized_start=503
  _RPCORDERCANCELREQUEST._serialized_end=571
  _RPCORDERCANCELRESPONSE._serialized_start=573
  _RPCORDERCANCELRESPONSE._serialized_end=662
  _RPCORDERREFILLREQUEST._serialized_start=664
  _RPCORDERREFILLREQUEST._serialized_end=732
  _RPCORDERREFILLRESPONSE._serialized_start=734
  _RPCORDERREFILLRESPONSE._serialized_end=823
  _RPCORDERSETAMOUNTREQUEST._serialized_start=825
  _RPCORDERSETAMOUNTREQUEST._serialized_end=896
  _RPCORDERSETAMOUNTRESPONSE._serialized_start=898
  _RPCORDERSETAMOUNTRESPONSE._serialized_end=990
  _RPCORDERSETLIMITREQUEST._serialized_start=992
  _RPCORDERSETLIMITREQUEST._serialized_end=1067
  _RPCORDERSETLIMITRESPONSE._serialized_start=1069
  _RPCORDERSETLIMITRESPONSE._serialized_end=1160
  _RPCORDERSETPRICEREQUEST._serialized_start=1162
  _RPCORDERSETPRICEREQUEST._serialized_end=1237
  _RPCORDERSETPRICERESPONSE._serialized_start=1239
  _RPCORDERSETPRICERESPONSE._serialized_end=1330
  _RPCORDERUPDATEREQUEST._serialized_start=1332
  _RPCORDERUPDATEREQUEST._serialized_end=1446
  _RPCORDERUPDATERESPONSE._serialized_start=1448
  _RPCORDERUPDATERESPONSE._serialized_end=1537
  _RPCRESPONSE._serialized_start=1539
  _RPCRESPONSE._serialized_end=1569
  _RPCRIGREQUEST._serialized_start=1572
  _RPCRIGREQUEST._serialized_end=1707
  _RPCRIGDATA._serialized_start=1709
  _RPCRIGDATA._serialized_end=1831
  _RPCRIGSUMMARYDATA._serialized_start=1834
  _RPCRIGSUMMARYDATA._serialized_end=2174
  _RPCORDERREQUEST._serialized_start=2177
  _RPCORDERREQUEST._serialized_end=2318
  _RPCORDERDATA._serialized_start=2321
  _RPCORDERDATA._serialized_end=2477
  _RPCORDERAMOUNTDATA._serialized_start=2479
  _RPCORDERAMOUNTDATA._serialized_end=2599
  _RPCORDERSUMMARYDATA._serialized_start=2602
  _RPCORDERSUMMARYDATA._serialized_end=2966
  _RPCPOOLSTAT._serialized_start=2969
  _RPCPOOLSTAT._serialized_end=3627
  _RPCBRIDGEDATA._serialized_start=3630
  _RPCBRIDGEDATA._serialized_end=3860
  _RPCBRIDGESDATASUM._serialized_start=3863
  _RPCBRIDGESDATASUM._serialized_end=4023
  _RPCPOOLBLOCKREWARDDATA._serialized_start=4026
  _RPCPOOLBLOCKREWARDDATA._serialized_end=4234
  _RPCPOOLGLOBALDIFFICULTIES._serialized_start=4236
  _RPCPOOLGLOBALDIFFICULTIES._serialized_end=4304
  _RPCSTRATUMSTATSSUMMARYREQUEST._serialized_start=4306
  _RPCSTRATUMSTATSSUMMARYREQUEST._serialized_end=4410
  _RPCSPEEDAMOUNTREQUEST._serialized_start=4412
  _RPCSPEEDAMOUNTREQUEST._serialized_end=4449
  _RPCSPEEDAMOUNTRESPONSE._serialized_start=4452
  _RPCSPEEDAMOUNTRESPONSE._serialized_end=4997
  _RPCSETPRICEREQUEST._serialized_start=4999
  _RPCSETPRICEREQUEST._serialized_end=5048
  _RPCSETPRICERESPONSE._serialized_start=5050
  _RPCSETPRICERESPONSE._serialized_end=5121
  _RPCRESPONSESTATUS._serialized_start=5123
  _RPCRESPONSESTATUS._serialized_end=5216
  _RPCRESPONSEERROR._serialized_start=5218
  _RPCRESPONSEERROR._serialized_end=5267
  _RPCSTRATUMWHITELISTREQUEST._serialized_start=5269
  _RPCSTRATUMWHITELISTREQUEST._serialized_end=5316
  _RPCSTRATUMWHITELISTRESPONSE._serialized_start=5318
  _RPCSTRATUMWHITELISTRESPONSE._serialized_end=5418
  _RPCSTRATUMWHITELISTADDREQUEST._serialized_start=5420
  _RPCSTRATUMWHITELISTADDREQUEST._serialized_end=5492
  _RPCSTRATUMWHITELISTADDRESPONSE._serialized_start=5494
  _RPCSTRATUMWHITELISTADDRESPONSE._serialized_end=5562
  _RPCSTRATUMWHITELISTREMOVEREQUEST._serialized_start=5564
  _RPCSTRATUMWHITELISTREMOVEREQUEST._serialized_end=5639
  _RPCSTRATUMWHITELISTREMOVERESPONSE._serialized_start=5641
  _RPCSTRATUMWHITELISTREMOVERESPONSE._serialized_end=5712
  _RPCBLACKLISTENTRY._serialized_start=5714
  _RPCBLACKLISTENTRY._serialized_end=5785
  _RPCSTRATUMBLACKLISTREQUEST._serialized_start=5787
  _RPCSTRATUMBLACKLISTREQUEST._serialized_end=5913
  _RPCSTRATUMBLACKLISTREMOVEREQUEST._serialized_start=5915
  _RPCSTRATUMBLACKLISTREMOVEREQUEST._serialized_end=6004
  _RPCSTRATUMBLACKLISTREMOVERESPONSE._serialized_start=6006
  _RPCSTRATUMBLACKLISTREMOVERESPONSE._serialized_end=6077
  _RPCSTRATUMBLACKLISTCLEARREQUEST._serialized_start=6079
  _RPCSTRATUMBLACKLISTCLEARREQUEST._serialized_end=6126
  _RPCSTRATUMBLACKLISTCLEARRESPONSE._serialized_start=6128
  _RPCSTRATUMBLACKLISTCLEARRESPONSE._serialized_end=6198
  _RPCSTRATUMALGOBRIDGECONFIG._serialized_start=6201
  _RPCSTRATUMALGOBRIDGECONFIG._serialized_end=6375
  _RPCSTRATUMALGORIGCONFIG._serialized_start=6378
  _RPCSTRATUMALGORIGCONFIG._serialized_end=6535
  _RPCSTRATUMALGOVALIDATORADDRESS._serialized_start=6537
  _RPCSTRATUMALGOVALIDATORADDRESS._serialized_end=6595
  _RPCSTRATUMALGOCONFIG._serialized_start=6598
  _RPCSTRATUMALGOCONFIG._serialized_end=6823
  _RPCSTRATUMALGOCONFIGGETREQUEST._serialized_start=6825
  _RPCSTRATUMALGOCONFIGGETREQUEST._serialized_end=6890
  _RPCSTRATUMALGOCONFIGGETRESPONSE._serialized_start=6892
  _RPCSTRATUMALGOCONFIGGETRESPONSE._serialized_end=6994
  _RPCSTRATUMALGOCONFIGSETREQUEST._serialized_start=6996
  _RPCSTRATUMALGOCONFIGSETREQUEST._serialized_end=7081
  _RPCSTRATUMALGOCONFIGSETRESPONSE._serialized_start=7083
  _RPCSTRATUMALGOCONFIGSETRESPONSE._serialized_end=7152
  _RPCMONITORINGALGORITHMSTATS._serialized_start=7154
  _RPCMONITORINGALGORITHMSTATS._serialized_end=7223
  _RPCMONITORINGORDERSSTATS._serialized_start=7226
  _RPCMONITORINGORDERSSTATS._serialized_end=7637
  _RPCMONITORINGRIGSSTATS._serialized_start=7640
  _RPCMONITORINGRIGSSTATS._serialized_end=8095
  _RPCMONITORINGVALIDATORSSTATS._serialized_start=8098
  _RPCMONITORINGVALIDATORSSTATS._serialized_end=8267
  _RPCMONITORINGPUSHSTATS._serialized_start=8269
  _RPCMONITORINGPUSHSTATS._serialized_end=8386
  _RPCMONITORINGALGORITHMREQUEST._serialized_start=8389
  _RPCMONITORINGALGORITHMREQUEST._serialized_end=8704
  _RPCMONITORINGSTRAND._serialized_start=8706
  _RPCMONITORINGSTRAND._serialized_end=8796
  _RPCMONITORINGSTRATUMREQUEST._serialized_start=8798
  _RPCMONITORINGSTRATUMREQUEST._serialized_end=8900
  _RIGORDERSTATISTIC._serialized_start=8903
  _RIGORDERSTATISTIC._serialized_end=9044
  _RIGORDERDATA._serialized_start=9046
  _RIGORDERDATA._serialized_end=9166
# @@protoc_insertion_point(module_scope)