import hashlib

try:
    from id_mapper import REAL_BATTERY_ID
except ImportError:
    REAL_BATTERY_ID = 'PLACEHOLDER_BATTERY'

battery_id_real     = REAL_BATTERY_ID
battery_id_hashed   = 'BATTERY_' + hashlib.sha256(REAL_BATTERY_ID.encode()).hexdigest()[:6]

battery_id_friendly = 'BATTERY_1'

def col_name(prefix: str, use_hashed: bool = False, use_friendly: bool = False) -> str:
    if use_friendly:
        return prefix + battery_id_friendly
    return prefix + (battery_id_hashed if use_hashed else battery_id_real)