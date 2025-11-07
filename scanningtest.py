import asyncio
from bleak import BleakScanner

async def main():
    print('Scanning for BLE devices (5s)...')
    devices = await BleakScanner.discover(timeout=5.0)
    if not devices:
        print('No BLE devices found')
    for d in devices:
        # print address, name, rssi
        print(f'{d.address} | {d.name!r} | RSSI={d.rssi}')

asyncio.run(main())