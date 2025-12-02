from django import template

register = template.Library()


@register.filter
def format_vnd(value):
    """
    Format a number as Vietnamese Dong (VND) currency.
    
    Converts numeric values to VND format with thousand separators using periods.
    
    Args:
        value: A numeric value (int, float, Decimal, or string representation)
               representing the price in VND.
    
    Returns:
        str: Formatted string like "65.000.000 VND" for input 65000000.
             Returns the original value if conversion fails.
    
    Examples:
        >>> format_vnd(65000000)
        '65.000.000 VND'
        >>> format_vnd(2800000)
        '2.800.000 VND'
    """
    try:
        # Convert to integer to remove decimal places
        value = int(value)
        # Format with thousand separators using period
        formatted = f"{value:,}".replace(",", ".")
        return f"{formatted} VND"
    except (ValueError, TypeError):
        return value
