from datetime import date, datetime, timedelta


def date_range(begin_dt, end_dt, parse_format="%Y-%m-%d", out_format="%Y-%m-%d", delta_type="day", delta=1):
    """接两个date 两个datetime 或者两个相同格式的str.
    Notes:
        输出迭代器不含最后一个

    Args:
        begin_dt     (date|datetime|str): 开始.
        end_dt       (date|datetime|str): 结束.
        parse_format (str): 输入间隔为字符串时的解析格式.
        out_format   (str): 输出时的格式.
        delta_type   (str): day | hour | minute | second.
        delta        (int: > 0): delta.

    Returns:
        iterator: 返回的格式化好的字符串展示迭代器

    Examples:
        >>> begin = date.today() + timedelta(days=-10)
        >>> end = date.today()

        >>> [dt for dt in date_range(begin, end, delta=5)]
        ['2018-05-05', '2018-05-10']
    """
    if isinstance(begin_dt, str):
        begin_dt = datetime.strptime(begin_dt, parse_format)

    if isinstance(end_dt, str):
        end_dt = datetime.strptime(end_dt, parse_format)

    range_delta = {
        "day": timedelta(days=delta),
        "hour": timedelta(hours=delta),
        "minute": timedelta(minutes=delta),
        "second": timedelta(seconds=delta),
    }

    t_dt = begin_dt
    while t_dt < end_dt:
        yield t_dt.strftime(out_format)
        t_dt = t_dt + range_delta[delta_type]
