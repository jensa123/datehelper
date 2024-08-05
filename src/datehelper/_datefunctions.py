"""Contains various date functions."""

from datetime import date, timedelta


def _coalesce_to_today(dt: date | None) -> date:
    if dt is None:
        return date.today()
    return dt


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


def first_day_of_month(dt: date | None) -> date:
    """Get the first day of the month of the given date.

    If argument is omitted or None then the first day of the month
    is calculated based on date.today().

    Args:
        dt: The relative date from which to calculate the first day of the month.
    Returns:
        The first day of the month.

    Examples::

        dt: date = date(2024, 8, 5)
        first: date = first_day_of_month(dt)  # 2024-08-01
    """
    dt = _coalesce_to_today(dt)
    return date(dt.year, dt.month, 1)
