#ifndef DODGE_PROJECTILE_EVALUATOR_H
#define DODGE_PROJECTILE_EVALUATOR_H

#include "Goal_Evaluator.h"
#include "../Raven_Bot.h"

class DodgeProjectileGoal_Evalutor : public Goal_Evaluator
{
public:
	DodgeProjectileGoal_Evalutor(double bias) : Goal_Evaluator(bias) {}

	double CalculateDesirability(Raven_Bot* pBot) override;
	void SetGoal(Raven_Bot* pBot) override;
	std::string GetName() { return "dodge_projectile"; }
	void  RenderInfo(Vector2D Position, Raven_Bot* pBot) {};
};

#endif