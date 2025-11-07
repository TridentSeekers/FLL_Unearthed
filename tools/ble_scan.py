import asyncio
from bleak import BleakScanner

async def main():
    print('Scanning for BLE devices for 6 seconds...')
    devices = await BleakScanner.discover(timeout=6.0)
    if not devices:
        print('No BLE devices found')
        return
    for d in devices:
        # Some bleak versions don't expose rssi as an attribute on BLEDevice.
        # Print safe summary (address, name) and repr/dev metadata when available.
        name = d.name
        addr = d.address
        print(f"{addr} | {name!r} | repr={repr(d)}")
        if hasattr(d, 'metadata') and d.metadata:
            print('  metadata:', d.metadata)
        if hasattr(d, 'details') and d.details:
            print('  details:', d.details)

if __name__ == '__main__':
    asyncio.run(main())
