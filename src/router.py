import responder

processes = [
    responder.Helo().main,
    responder.Rejoin().main,
    responder.Go().main,
    responder.Taikyoku().main,
    responder.Init().main,
    responder.Tsumo().main,
    responder.Dahai().main,
    responder.Naki().main,
    responder.ReachStep1().main,
    responder.ReachStep2().main,
    responder.Dora().main,
    responder.Agari().main,
    responder.Ryuukyoku().main,
    responder.End().main,
]
