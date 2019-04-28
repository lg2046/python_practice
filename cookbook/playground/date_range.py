from datetime import datetime, timedelta


def time_range(begin_dt, end_dt):
    if isinstance(begin_dt, str):
        begin_dt = datetime.strptime(begin_dt, "%Y-%m-%d").date()

    if isinstance(end_dt, str):
        end_dt = datetime.strptime(end_dt, "%Y-%m-%d").date()

    t_dt = begin_dt
    while t_dt < end_dt:
        yield t_dt
        t_dt = t_dt + timedelta(days=1)


begin = "2018-01-01"
end = "2019-12-31"

# 不含最后一个
print(','.join([str(t) for t in time_range(begin, end)]))
