# (C) Datadog, Inc. 2018-present
# All rights reserved
# Licensed under a 3-clause BSD style license (see LICENSE)
METRIC_MAP = {
    'addsstable_applications': 'addsstable.applications',
    'addsstable_copies': 'addsstable.copies',
    'addsstable_proposals': 'addsstable.proposals',
    'capacity': 'capacity.total',
    'capacity_available': 'capacity.available',
    'capacity_reserved': 'capacity.reserved',
    'capacity_used': 'capacity.used',
    'clock_offset_meannanos': 'clock.offset.meannanos',
    'clock_offset_stddevnanos': 'clock.offset.stddevnanos',
    'compactor_compactingnanos': 'compactor.compactingnanos',
    'compactor_compactions_failure': 'compactor.compactions.failure',
    'compactor_compactions_success': 'compactor.compactions.success',
    'compactor_suggestionbytes_compacted': 'compactor.suggestionbytes.compacted',
    'compactor_suggestionbytes_queued': 'compactor.suggestionbytes.queued',
    'compactor_suggestionbytes_skipped': 'compactor.suggestionbytes.skipped',
    'distsender_batches_partial': 'distsender.batches.partial',
    'distsender_batches': 'distsender.batches.total',
    'distsender_errors_notleaseholder': 'distsender.errors.notleaseholder',
    'distsender_rpc_sent_local': 'distsender.rpc.sent.local',
    'distsender_rpc_sent_nextreplicaerror': 'distsender.rpc.sent.nextreplicaerror',
    'distsender_rpc_sent': 'distsender.rpc.sent.total',
    'exec_error': 'exec.error',
    'exec_latency': 'exec.latency',
    'exec_success': 'exec.success',
    'gcbytesage': 'gcbytesage',
    'gossip_bytes_received': 'gossip.bytes.received',
    'gossip_bytes_sent': 'gossip.bytes.sent',
    'gossip_connections_incoming': 'gossip.connections.incoming',
    'gossip_connections_outgoing': 'gossip.connections.outgoing',
    'gossip_connections_refused': 'gossip.connections.refused',
    'gossip_infos_received': 'gossip.infos.received',
    'gossip_infos_sent': 'gossip.infos.sent',
    'intentage': 'intentage',
    'intentbytes': 'intentbytes',
    'intentcount': 'intentcount',
    'keybytes': 'keybytes',
    'keycount': 'keycount',
    'lastupdatenanos': 'lastupdatenanos',
    'leases_epoch': 'leases.epoch',
    'leases_error': 'leases.error',
    'leases_expiration': 'leases.expiration',
    'leases_success': 'leases.success',
    'leases_transfers_error': 'leases.transfers.error',
    'leases_transfers_success': 'leases.transfers.success',
    'livebytes': 'livebytes',
    'livecount': 'livecount',
    'liveness_epochincrements': 'liveness.epochincrements',
    'liveness_heartbeatfailures': 'liveness.heartbeatfailures',
    'liveness_heartbeatlatency': 'liveness.heartbeatlatency',
    'liveness_heartbeatsuccesses': 'liveness.heartbeatsuccesses',
    'liveness_livenodes': 'liveness.livenodes',
    'node_id': 'node_id',
    'queue_consistency_pending': 'queue.consistency.pending',
    'queue_consistency_process_failure': 'queue.consistency.process.failure',
    'queue_consistency_process_success': 'queue.consistency.process.success',
    'queue_consistency_processingnanos': 'queue.consistency.processingnanos',
    'queue_gc_info_abortspanconsidered': 'queue.gc.info.abortspanconsidered',
    'queue_gc_info_abortspangcnum': 'queue.gc.info.abortspangcnum',
    'queue_gc_info_abortspanscanned': 'queue.gc.info.abortspanscanned',
    'queue_gc_info_intentsconsidered': 'queue.gc.info.intentsconsidered',
    'queue_gc_info_intenttxns': 'queue.gc.info.intenttxns',
    'queue_gc_info_numkeysaffected': 'queue.gc.info.numkeysaffected',
    'queue_gc_info_pushtxn': 'queue.gc.info.pushtxn',
    'queue_gc_info_resolvesuccess': 'queue.gc.info.resolvesuccess',
    'queue_gc_info_resolvetotal': 'queue.gc.info.resolvetotal',
    'queue_gc_info_transactionspangcaborted': 'queue.gc.info.transactionspangcaborted',
    'queue_gc_info_transactionspangccommitted': 'queue.gc.info.transactionspangccommitted',
    'queue_gc_info_transactionspangcpending': 'queue.gc.info.transactionspangcpending',
    'queue_gc_info_transactionspanscanned': 'queue.gc.info.transactionspanscanned',
    'queue_gc_pending': 'queue.gc.pending',
    'queue_gc_process_failure': 'queue.gc.process.failure',
    'queue_gc_process_success': 'queue.gc.process.success',
    'queue_gc_processingnanos': 'queue.gc.processingnanos',
    'queue_raftlog_pending': 'queue.raftlog.pending',
    'queue_raftlog_process_failure': 'queue.raftlog.process.failure',
    'queue_raftlog_process_success': 'queue.raftlog.process.success',
    'queue_raftlog_processingnanos': 'queue.raftlog.processingnanos',
    'queue_raftsnapshot_pending': 'queue.raftsnapshot.pending',
    'queue_raftsnapshot_process_failure': 'queue.raftsnapshot.process.failure',
    'queue_raftsnapshot_process_success': 'queue.raftsnapshot.process.success',
    'queue_raftsnapshot_processingnanos': 'queue.raftsnapshot.processingnanos',
    'queue_replicagc_pending': 'queue.replicagc.pending',
    'queue_replicagc_process_failure': 'queue.replicagc.process.failure',
    'queue_replicagc_process_success': 'queue.replicagc.process.success',
    'queue_replicagc_processingnanos': 'queue.replicagc.processingnanos',
    'queue_replicagc_removereplica': 'queue.replicagc.removereplica',
    'queue_replicate_addreplica': 'queue.replicate.addreplica',
    'queue_replicate_pending': 'queue.replicate.pending',
    'queue_replicate_process_failure': 'queue.replicate.process.failure',
    'queue_replicate_process_success': 'queue.replicate.process.success',
    'queue_replicate_processingnanos': 'queue.replicate.processingnanos',
    'queue_replicate_purgatory': 'queue.replicate.purgatory',
    'queue_replicate_rebalancereplica': 'queue.replicate.rebalancereplica',
    'queue_replicate_removedeadreplica': 'queue.replicate.removedeadreplica',
    'queue_replicate_removereplica': 'queue.replicate.removereplica',
    'queue_replicate_transferlease': 'queue.replicate.transferlease',
    'queue_split_pending': 'queue.split.pending',
    'queue_split_process_failure': 'queue.split.process.failure',
    'queue_split_process_success': 'queue.split.process.success',
    'queue_split_processingnanos': 'queue.split.processingnanos',
    'queue_tsmaintenance_pending': 'queue.tsmaintenance.pending',
    'queue_tsmaintenance_process_failure': 'queue.tsmaintenance.process.failure',
    'queue_tsmaintenance_process_success': 'queue.tsmaintenance.process.success',
    'queue_tsmaintenance_processingnanos': 'queue.tsmaintenance.processingnanos',
    'raft_commandsapplied': 'raft.commandsapplied',
    'raft_enqueued_pending': 'raft.enqueued.pending',
    'raft_heartbeats_pending': 'raft.heartbeats.pending',
    'raft_process_commandcommit_latency': 'raft.process.commandcommit.latency',
    'raft_process_logcommit_latency': 'raft.process.logcommit.latency',
    'raft_process_tickingnanos': 'raft.process.tickingnanos',
    'raft_process_workingnanos': 'raft.process.workingnanos',
    'raft_rcvd_app': 'raft.rcvd.app',
    'raft_rcvd_appresp': 'raft.rcvd.appresp',
    'raft_rcvd_dropped': 'raft.rcvd.dropped',
    'raft_rcvd_heartbeat': 'raft.rcvd.heartbeat',
    'raft_rcvd_heartbeatresp': 'raft.rcvd.heartbeatresp',
    'raft_rcvd_prevote': 'raft.rcvd.prevote',
    'raft_rcvd_prevoteresp': 'raft.rcvd.prevoteresp',
    'raft_rcvd_prop': 'raft.rcvd.prop',
    'raft_rcvd_snap': 'raft.rcvd.snap',
    'raft_rcvd_timeoutnow': 'raft.rcvd.timeoutnow',
    'raft_rcvd_transferleader': 'raft.rcvd.transferleader',
    'raft_rcvd_vote': 'raft.rcvd.vote',
    'raft_rcvd_voteresp': 'raft.rcvd.voteresp',
    'raft_ticks': 'raft.ticks',
    'raftlog_behind': 'raftlog.behind',
    'raftlog_truncated': 'raftlog.truncated',
    'range_adds': 'range.adds',
    'range_raftleadertransfers': 'range.raftleadertransfers',
    'range_removes': 'range.removes',
    'range_snapshots_generated': 'range.snapshots.generated',
    'range_snapshots_normal_applied': 'range.snapshots.normal_applied',
    'range_snapshots_preemptive_applied': 'range.snapshots.preemptive_applied',
    'range_splits': 'range.splits.total',
    'ranges': 'ranges',
    'ranges_unavailable': 'ranges.unavailable',
    'ranges_underreplicated': 'ranges.underreplicated',
    'rebalancing_writespersecond': 'rebalancing.writespersecond',
    'replicas_commandqueue_combinedqueuesize': 'replicas.commandqueue.combinedqueuesize',
    'replicas_commandqueue_combinedreadcount': 'replicas.commandqueue.combinedreadcount',
    'replicas_commandqueue_combinedwritecount': 'replicas.commandqueue.combinedwritecount',
    'replicas_commandqueue_maxoverlaps': 'replicas.commandqueue.maxoverlaps',
    'replicas_commandqueue_maxreadcount': 'replicas.commandqueue.maxreadcount',
    'replicas_commandqueue_maxsize': 'replicas.commandqueue.maxsize',
    'replicas_commandqueue_maxtreesize': 'replicas.commandqueue.maxtreesize',
    'replicas_commandqueue_maxwritecount': 'replicas.commandqueue.maxwritecount',
    'replicas_leaders': 'replicas.leaders',
    'replicas_leaders_not_leaseholders': 'replicas.leaders.not_leaseholders',
    'replicas_leaseholders': 'replicas.leaseholders',
    'replicas_quiescent': 'replicas.quiescent',
    'replicas_reserved': 'replicas.reserved',
    'replicas': 'replicas.total',
    'requests_backpressure_split': 'requests.backpressure.split',
    'requests_slow_commandqueue': 'requests.slow.commandqueue',
    'requests_slow_distsender': 'requests.slow.distsender',
    'requests_slow_lease': 'requests.slow.lease',
    'requests_slow_raft': 'requests.slow.raft',
    'rocksdb_block_cache_hits': 'rocksdb.block.cache.hits',
    'rocksdb_block_cache_misses': 'rocksdb.block.cache.misses',
    'rocksdb_block_cache_pinned_usage': 'rocksdb.block.cache.pinned.usage',
    'rocksdb_block_cache_usage': 'rocksdb.block.cache.usage',
    'rocksdb_bloom_filter_prefix_checked': 'rocksdb.bloom_filter.prefix.checked',
    'rocksdb_bloom_filter_prefix_useful': 'rocksdb.bloom_filter.prefix.useful',
    'rocksdb_compactions': 'rocksdb.compactions.total',
    'rocksdb_flushes': 'rocksdb.flushes.total',
    'rocksdb_memtable_total_size': 'rocksdb.memtable.total.size',
    'rocksdb_num_sstables': 'rocksdb.num_sstables',
    'rocksdb_read_amplification': 'rocksdb.read.amplification',
    'rocksdb_table_readers_mem_estimate': 'rocksdb.table.readers.mem.estimate',
    'round_trip_latency': 'round_trip.latency',
    'schedules_BACKUP_failed': 'schedules.backup.failed',
    'schedules_BACKUP_started': 'schedules.backup.started',
    'schedules_BACKUP_succeeded': 'schedules.backup.succeeded',
    'sql_bytesin': 'sql.bytesin',
    'sql_bytesout': 'sql.bytesout',
    'sql_conns': 'sql.conns',
    'sql_ddl_count': 'sql.ddl.count',
    'sql_delete_count': 'sql.delete.count',
    'sql_distsql_exec_latency': 'sql.distsql.exec.latency',
    'sql_distsql_flows_active': 'sql.distsql.flows.active',
    'sql_distsql_flows_total': 'sql.distsql.flows.total',
    'sql_distsql_queries_active': 'sql.distsql.queries.active',
    'sql_distsql_queries_total': 'sql.distsql.queries.total',
    'sql_distsql_select_count': 'sql.distsql.select.count',
    'sql_distsql_service_latency': 'sql.distsql.service.latency',
    'sql_exec_latency': 'sql.exec.latency',
    'sql_insert_count': 'sql.insert.count',
    'sql_mem_admin_current': 'sql.mem.admin.current',
    'sql_mem_admin_max': 'sql.mem.admin.max',
    'sql_mem_admin_session_current': 'sql.mem.admin.session.current',
    'sql_mem_admin_session_max': 'sql.mem.admin.session.max',
    'sql_mem_admin_txn_current': 'sql.mem.admin.txn.current',
    'sql_mem_admin_txn_max': 'sql.mem.admin.txn.max',
    'sql_mem_client_current': 'sql.mem.client.current',
    'sql_mem_client_max': 'sql.mem.client.max',
    'sql_mem_client_session_current': 'sql.mem.client.session.current',
    'sql_mem_client_session_max': 'sql.mem.client.session.max',
    'sql_mem_client_txn_current': 'sql.mem.client.txn.current',
    'sql_mem_client_txn_max': 'sql.mem.client.txn.max',
    'sql_mem_conns_current': 'sql.mem.conns.current',
    'sql_mem_conns_max': 'sql.mem.conns.max',
    'sql_mem_conns_session_current': 'sql.mem.conns.session.current',
    'sql_mem_conns_session_max': 'sql.mem.conns.session.max',
    'sql_mem_conns_txn_current': 'sql.mem.conns.txn.current',
    'sql_mem_conns_txn_max': 'sql.mem.conns.txn.max',
    'sql_mem_distsql_current': 'sql.mem.distsql.current',
    'sql_mem_distsql_max': 'sql.mem.distsql.max',
    'sql_mem_internal_current': 'sql.mem.internal.current',
    'sql_mem_internal_max': 'sql.mem.internal.max',
    'sql_mem_internal_session_current': 'sql.mem.internal.session.current',
    'sql_mem_internal_session_max': 'sql.mem.internal.session.max',
    'sql_mem_internal_txn_current': 'sql.mem.internal.txn.current',
    'sql_mem_internal_txn_max': 'sql.mem.internal.txn.max',
    'sql_misc_count': 'sql.misc.count',
    'sql_query_count': 'sql.query.count',
    'sql_select_count': 'sql.select.count',
    'sql_service_latency': 'sql.service.latency',
    'sql_txn_abort_count': 'sql.txn.abort.count',
    'sql_txn_begin_count': 'sql.txn.begin.count',
    'sql_txn_commit_count': 'sql.txn.commit.count',
    'sql_txn_rollback_count': 'sql.txn.rollback.count',
    'sql_update_count': 'sql.update.count',
    'sys_cgo_allocbytes': 'sys.cgo.allocbytes',
    'sys_cgo_totalbytes': 'sys.cgo.totalbytes',
    'sys_cgocalls': 'sys.cgocalls',
    'sys_cpu_sys_ns': 'sys.cpu.sys.ns',
    'sys_cpu_sys_percent': 'sys.cpu.sys.percent',
    'sys_cpu_user_ns': 'sys.cpu.user.ns',
    'sys_cpu_user_percent': 'sys.cpu.user.percent',
    'sys_fd_open': 'sys.fd.open',
    'sys_fd_softlimit': 'sys.fd.softlimit',
    'sys_gc_count': 'sys.gc.count',
    'sys_gc_pause_ns': 'sys.gc.pause.ns',
    'sys_gc_pause_percent': 'sys.gc.pause.percent',
    'sys_go_allocbytes': 'sys.go.allocbytes',
    'sys_go_totalbytes': 'sys.go.totalbytes',
    'sys_goroutines': 'sys.goroutines',
    'sys_rss': 'sys.rss',
    'sys_uptime': 'sys.uptime',
    'sysbytes': 'sysbytes',
    'syscount': 'syscount',
    'timeseries_write_bytes': 'timeseries.write.bytes',
    'timeseries_write_errors': 'timeseries.write.errors',
    'timeseries_write_samples': 'timeseries.write.samples',
    'totalbytes': 'totalbytes',
    'tscache_skl_read_pages': 'tscache.skl.read.pages',
    'tscache_skl_read_rotations': 'tscache.skl.read.rotations',
    'tscache_skl_write_pages': 'tscache.skl.write.pages',
    'tscache_skl_write_rotations': 'tscache.skl.write.rotations',
    'txn_abandons': 'txn.abandons',
    'txn_aborts': 'txn.aborts',
    'txn_autoretries': 'txn.autoretries',
    'txn_commits': 'txn.commits',
    'txn_commits1PC': 'txn.commits1PC',
    'txn_durations': 'txn.durations',
    'txn_restarts': 'txn.restarts',
    'txn_restarts_deleterange': 'txn.restarts.deleterange',
    'txn_restarts_possiblereplay': 'txn.restarts.possiblereplay',
    'txn_restarts_serializable': 'txn.restarts.serializable',
    'txn_restarts_writetooold': 'txn.restarts.writetooold',
    'valbytes': 'valbytes',
    'valcount': 'valcount',
    'admission_wait_sum_kv': 'admission.wait.sum.kv',
    'admission_wait_sum_kv_stores': 'admission.wait.sum.kv_stores',
    'admission_wait_sum_sql_kv_response': 'admission.wait.sum.sql_kv.response',
    'admission_wait_sum_sql_sql_response': 'admission.wait.sum.sql_sql.response',
    'changefeed_backfill_count': 'changefeed.backfill',
    'changefeed_backfill_pending_ranges': 'changefeed.backfill.pending.ranges',
    'changefeed_commit_latency': 'changefeed.commit.latency',
    'changefeed_emitted_messages': 'changefeed.emitted.messages',
    'changefeed_error_retries': 'changefeed.error.retries',
    'changefeed_failures': 'changefeed.failures',
    'changefeed_max_behind_nanos': 'changefeed.max.behind.nanos',
    'changefeed_message_size_hist': 'changefeed.message.size.hist',
    'changefeed_running': 'changefeed.running',
    'jobs_changefeed_resume_retry_error': 'jobs.changefeed.resume.retry.error',
    'ranges_overreplicated': 'ranges.overreplicated',
    'rocksdb.compactions.total': 'rocksdb.compactions',
    'sql_conn_latency': 'sql.conn.latency',
    'sql_distsql_contended_queries_count': 'sql.distsql.contended.queries',
    'sql_failure_count': 'sql.failure',
    'sql_full_scan_count': 'sql.full.scan',
    'sql_statements_active': 'sql.statements.active',
    'sql_txn_latency': 'sql.txn.latency',
    'sql_txns_open': 'sql.txns.open',
    'sys_cpu_combined_percent_normalized': 'sys.cpu.combined.percent.normalized',
    'sys_host_net_recv_bytes': 'sys.host.net.recv.bytes',
    'sys_host_net_send_bytes': 'sys.host.net.send.bytes',
    'sys_host_disk_read_bytes': 'sys.host.disk.read.bytes',
    'sys_host_disk_write_bytes': 'sys.host.disk.write.bytes',
    'admission_requested_kv': 'admission.requested.kv',
    'admission_requested_kv_stores': 'admission.requested.kv_stores',
    'admission_admitted_sql_sql_response': 'admission.admitted.sql_sql.response',
    'admission_admitted_sql_leaf_start': 'admission.admitted.sql.leaf.start',
    'admission_granter_total_slots_kv': 'admission.granter.total.slots.kv',
    'admission_wait_queue_length_sql_sql_response': 'admission.wait.queue.length.sql_sql.response',
    'admission_granter_used_slots_kv': 'admission.granter.used.slots.kv',
    'admission_errored_sql_root_start': 'admission.errored.sql.root.start',
    'admission_wait_queue_length_kv': 'admission.wait.queue.length.kv',
    'admission_errored_kv': 'admission.errored.kv',
    'admission_requested_sql_leaf_start': 'admission.requested.sql.leaf.start',
    'admission_errored_sql_leaf_start': 'admission.errored.sql.leaf.start',
    'admission_wait_sum_sql_root_start': 'admission.wait.sum.sql.root.start',
    'admission_admitted_kv': 'admission.admitted.kv',
    'admission_admitted_sql_kv_response': 'admission.admitted.sql_kv.response',
    'admission_granter_used_slots_sql_root_start': 'admission.granter.used.slots.sql.root.start',
    'admission_wait_durations_kv': 'admission.wait.durations.kv',
    'admission_wait_durations_kv_stores': 'admission.wait.durations.kv_stores',
    'admission_wait_queue_length_sql_root_start': 'admission.wait.queue.lengths.sql.root.start',
    'admission_wait_queue_length_sql_kv_response': 'admission.wait.queue.length.sql_kv.response',
    'admission_wait_durations_sql_leaf_start': 'admission.wait.durations.sql.leaf.start',
    'admission_admitted_sql_root_start': 'admission.admitted.sql.root.start',
    'admission_granter_io_tokens_exhausted_duration_kv': 'admission.granter.io.tokens.exhausted.duration.kv',
    'admission_requested_sql_sql_response': 'admission.requested.sql_sql.response',
    'admission_wait_durations_sql_sql_response': 'admission.wait.durations.sql_sql.response',
    'admission_errored_sql_kv_response': 'admission.errored.sql_kv.response',
    'admission_requested_sql_kv_response': 'admission.requested.sql_kv.response',
    'admission_wait_queue_length_sql_leaf_start': 'admission.wait.queue.length.sql.leaf.start',
    'admission_wait_durations_sql_kv_response': 'admission.wait.durations.sql_kv.response',
    'admission_errored_kv_stores': 'admission.errored.kv_stores',
    'admission_requested_sql_root_start ': 'admission.requested.sql.root.start',
    'admission_granter_used_slots_sql_leaf_start': 'admission.granter.used.slots.sql.leaf.start',
    'admission_wait_sum_sql_kv_response ': 'admission.wait.sum.sql_kv.response',
    'admission_errored_sql_sql_response': 'admission.errored.sql_sql.response',
    'admission_admitted_kv_stores': 'admission.admitted.kv_stores',
    'changefeed_admit_latency': 'changefeed.admit.latency',
    'admission_wait_queue_length_kv_stores': 'admission.wait.queue.length.kv_stores',
    'jobs_backup_fail_or_cancel_completed ': 'jobs.backup.fail_or_cancel_completed',
    'jobs_backup_currently_running': 'jobs.backup.currently_running',
    'jobs_backup_currently_idle': 'jobs.backup.currently_idle',
    'jobs_backup_fail_or_cancel_retry_error': 'jobs.backup.fail_or_cancel_retry_error',
    'jobs_backup_fail_or_cancel_failed': 'jobs.backup.fail_or_cancel_failed',
    'jobs_backup_resume_failed': 'jobs.backup.resume_failed',
    'jobs_backup_resume_retry_error': 'jobs.backup.resume_retry_error',
    'jobs_backup_resume_completed ': 'jobs.backup.resume_completed',
    'schedules_BACKUP_last_completed_time': 'schedules.backup.last_completed_time',
}


def construct_metrics_config(metric_map, type_overrides):
    metrics = []
    for raw_metric_name, metric_name in metric_map.items():
        if raw_metric_name.endswith('_total'):
            raw_metric_name = raw_metric_name[:-6]
            metric_name = metric_name[:-6]
        elif metric_name.endswith('.count'):
            metric_name = metric_name[:-6]

        config = {raw_metric_name: {'name': metric_name}}
        if raw_metric_name in type_overrides:
            config[raw_metric_name]['type'] = type_overrides[raw_metric_name]

        metrics.append(config)

    return metrics
