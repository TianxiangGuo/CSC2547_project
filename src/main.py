import attacker
import defender
import target
import judge

def main():
    print("来电子斗蛐蛐吧")
    improvement, attack_prompt = attacker.attack()
    print("Attack:",attack_prompt)
    defend_prompt = defender.defend(attack_prompt)
    print("\nDefend:",defend_prompt)
    response = target.respond(defend_prompt)
    print("\nResponse:",response)
    judge_result = judge.judge(response)
    print("\nJudge:",judge_result)


if __name__ == "__main__":
    main()
