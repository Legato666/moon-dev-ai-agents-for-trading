"""
🌙 Moon Dev's Configuration File
Built with love by Moon Dev 🚀
"""

# 🔑 API Configuration
AI_MODEL = "claude-3-opus-20240229"
AI_MAX_TOKENS = 4096
AI_TEMPERATURE = 0.7

# 💰 Trading Configuration
USDC_ADDRESS = "EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v"  # Never trade or close
SOL_ADDRESS = "So11111111111111111111111111111111111111111"   # Never trade or close

# Create a list of addresses to exclude from trading/closing
EXCLUDED_TOKENS = [USDC_ADDRESS, SOL_ADDRESS]

# Token List for Trading 📋
MONITORED_TOKENS = [
    '9BB6NFEcjBCtnNLFko2FqVQBq8HHM13kCyYcdQbgpump',    # 🌬️ FART
    # 'EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v',    # 💵 USDC
    'HeLp6NuQkmYB4pYWo2zYs22mESHXPQYzXbB8n4V98jwC',    # 🤖 AI16Z
    'v62Jv9pwMTREWV9f6TetZfMafV254vo99p7HSF25BPr',     # 🎮 GG Solana
    'KENJSUYLASHUMfHyy5o4Hp2FdNqZg1AsUPhfH2kYvEP',   # GRIFFAIN
    # '8x5VqbHA8D7NkD52uNuS5nnt3PwA3pLD34ymskeSo2Wn',    # 🧠 ZEREBRO
    # 'Df6yfrKC8kZE3KNkrHERKzAetSxbrWeniQfyJY4Jpump',    # 😎 CHILL GUY
    # 'ED5nyyWEzpPPiWimP8vYm7sD7TD3LAt3Q3gRTWHzPJBY',    # 🌙 MOODENG
    # 'EKpQGSJtjMFqKZ9KQanSqYXRcF8fBopzLHYxdM65zcjm',    # 🐕 WIF
]

# Moon Dev's Token Trading List 🚀
# Each token is carefully selected by Moon Dev for maximum moon potential! 🌙
tokens_to_trade = MONITORED_TOKENS  # Using the same list for trading

# Token and wallet settings
symbol = '9BB6NFEcjBCtnNLFko2FqVQBq8HHM13kCyYcdQbgpump'
address = '4wgfCBf2WwLSRKLef9iW7JXZ2AfkxUxGM4XcKpHm3Sin'

# Position sizing 🎯
usd_size = 25  # Size of position to hold
max_usd_order_size = 1  # Max order size
tx_sleep = 30  # Sleep between transactions
slippage = 199  # Slippage settings

# Risk Management Settings 🛡️
CASH_PERCENTAGE = 20  # Minimum % to keep in USDC as safety buffer (0-100)
MAX_POSITION_PERCENTAGE = 30  # Maximum % allocation per position (0-100)
STOPLOSS_PRICE = 1
BREAKOUT_PRICE = .0001
SLEEP_AFTER_CLOSE = 600  # Prevent overtrading
DAILY_MAX_LOSS = .001 # in USDC - this is the max loss per day
DAILY_MAX_GAIN = .001 # in USDC - this is the max gain per day
MAX_LOSS_GAIN_CHECK_HOURS = 12  # How far back to check for max loss/gain limits (in hours)
SLEEP_BETWEEN_RUNS_MINUTES = 15  # How long to sleep between agent runs 🕒

# Transaction settings ⚡
slippage = 199  # 50% slippage, 500 = 5% and 50 = .5% slippage
PRIORITY_FEE = 100000  # ~0.02 USD at current SOL prices
orders_per_open = 3  # Multiple orders for better fill rates

# Market maker settings 📊
buy_under = .0946
sell_over = 1

# Data collection settings 📈
DAYSBACK_4_DATA = 3
DATA_TIMEFRAME = '3m'  # 1m, 3m, 5m, 15m, 30m, 1H, 2H, 4H, 6H, 8H, 12H, 1D, 3D, 1W, 1M
SAVE_OHLCV_DATA = False  # 🌙 Set to True to save data permanently, False will only use temp data during run

# AI Model Settings 🤖
AI_MODEL = "claude-3-haiku-20240307"  # Claude model to use: claude-3-haiku-20240307,claude-3-sonnet-20240229, claude-3-opus-20240229
AI_MAX_TOKENS = 1024  # Max tokens for response
AI_TEMPERATURE = 0.7  # Creativity vs precision (0-1)

USDC_ADDRESS = 'EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v'


# Future variables (not active yet) 🔮
sell_at_multiple = 3
USDC_SIZE = 1
limit = 49
timeframe = '15m'
stop_loss_perctentage = -.24
EXIT_ALL_POSITIONS = False
DO_NOT_TRADE_LIST = ['777']
CLOSED_POSITIONS_TXT = '777'
minimum_trades_in_last_hour = 777