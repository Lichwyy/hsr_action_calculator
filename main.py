# Constantes

TOTAL_AV = 10000
ZERO_CYCLE = 150
CYCLE = 100

speed = 134
amount_actions = 0
current_av = 0


class HsrActionsCalculator:
    def __init__(self, speed):
        self.speed = speed

    def actions_per_cycle(self, cycles):
        av_used = ZERO_CYCLE+(CYCLE*(cycles-1))
        current_av = TOTAL_AV/self.speed
        amount_actions = av_used/current_av
        return amount_actions

    def speed_break_points(self, actions, cycles):
        av_used = ZERO_CYCLE+(CYCLE*(cycles-1))
        current_av = av_used/actions
        speed = TOTAL_AV/current_av
        return speed
    
    def action_advancing(self, w):

testando = HsrActionsCalculator(200)

print(testando.actions_per_cycle(2))

print(testando.speed_break_points(5, 2))
