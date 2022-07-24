from pycoingecko import CoinGeckoAPI
import locale
from datetime import datetime
import tzlocal

local_timezone = tzlocal.get_localzone()
locale.setlocale(locale.LC_ALL, 'en_US')

cg = CoinGeckoAPI()
currency = input('Input the currency you would like to compare the price to, e.g. "usd": ').lower().strip()
coins = input('Input a list of coins you would like to check the price of: ').lower()

coin_list = [coin.strip() for coin in coins.split(',')]
for coin in coin_list:
    info_dict = cg.get_price(ids=coin, vs_currencies=currency, include_market_cap='true', include_24hr_vol='true', include_24hr_change='true', include_last_updated_at='true')[coin]
    price = info_dict[currency]

    mkt_cap = info_dict[f'{currency}_market_cap']
    readable_m_cap = locale.format_string("%d", int(round(mkt_cap, 0)), grouping=True)

    volume = info_dict[f'{currency}_24h_vol']
    readable_volume = locale.format_string("%d", int(round(volume, 0)), grouping=True)

    change = info_dict[f'{currency}_24h_change']

    ts = float(info_dict['last_updated_at'])
    local_time = datetime.fromtimestamp(ts, local_timezone)
    update_time = local_time.strftime("%Y-%m-%d %H:%M:%S (%Z)")

    print('\n')
    print(f'The current price of {coin.title()} is {round(price, 2)} {currency.upper()} with a market cap of {readable_m_cap} {currency.upper()}.')
    print(f'The price has changed by {round(change, 2)}% with a trading volume of {readable_volume} {currency.upper()} in the past 24 hours.')
    print(f'Last updated {update_time}.')
    print('\n')

bruh = input('Press ENTER to exit')