"""Contains various date functions."""

from datetime import date, timedelta


def _coalesce_to_today(dt: date | None) -> date:
    if dt is None:
        return date.today()
    return dt


def _is_weekend(dt: date) -> bool:
    return dt.isoweekday() in (6, 7)


def previous_business_day(dt: date | None = None) -> date:
    """Get the previous business day. A business day is defined
    as any weekday other than Saturday and Sunday.

    If argument is omitted or None then the previous business day
    is calculated based on date.today().

    Args:
        dt: The relative date from which to calculate the previous business day.
    Returns:
        The previous business day based on argument dt.

    Examples::

        dt: date = date(2024, 8, 5)
        prev_bus_day: date = previous_business_day(dt)  # 2024-08-02
    """
    dt = _coalesce_to_today(dt)
    wd: int = dt.isoweekday()
    sub: int = 1
    if wd == 7:
        sub = 2
    elif wd == 1:
        sub = 3
    return dt - timedelta(days=sub)


def first_day_of_month(
    dt: date | None = None, /, *, business_day: bool = False
) -> date:
    """Get the first day of the month of the given date.

    If argument is omitted or None then the first day of the month
    is calculated based on date.today().

    Args:
        dt: The relative date from which to calculate the first day of the month.
        business_day: If True then the first business day of the month will be returned.
    Returns:
        The first day of the month.

    Examples::

        dt: date = date(2024, 8, 5)
        first: date = first_day_of_month(dt)  # 2024-08-01
    """
    dt = _coalesce_to_today(dt)
    result: date = date(dt.year, dt.month, 1)
    if business_day and _is_weekend(result):
        return next_business_day(result)
    return result


def next_business_day(dt: date | None = None) -> date:
    """Get the next business day based on a given date.

    Args:
        dt: The relative date from which to calculate the next business day.
    Returns:
        The next business day.
    """
    dt = _coalesce_to_today(dt)
    wd: int = dt.isoweekday()
    add: int = 1
    if wd == 5:
        add = 3
    elif wd == 6:
        add = 2
    return dt + timedelta(days=add)


def first_day_of_year(
    dt: date | None = None, /, *, business_day: bool = False
) -> date:
    """Get the first day of the year relative to dt. If argument dt is omitted
    the first day of the year is calculated relative to date.today().

    Args:
        dt: The relative date from which to calculate the first day of the year.
        business_day: If True then the first business day of the year will be returned.
    Returns:
        The first day of the year.

    Examples::

        dt: date = date(2024, 8, 6)
        first: date = first_day_of_year(dt)  # 2024-01-01
    """
    dt: date = _coalesce_to_today(dt)
    result: date = date(dt.year, 1, 1)
    if business_day and _is_weekend(result):
        return next_business_day(result)
    return result
