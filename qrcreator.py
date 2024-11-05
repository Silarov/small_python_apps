import qrcode

qr = qrcode.make('https://calendar.google.com/calendar/u/0/appointments/AcZssZ0NnrteGDVkYObZ5BhFhkXI40nvVlD3HGn35j0=')
qr.save('QR.png')