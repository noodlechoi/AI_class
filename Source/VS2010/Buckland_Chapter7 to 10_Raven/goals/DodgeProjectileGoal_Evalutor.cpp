#include "../Raven_Bot.h"
#include "Raven_Feature.h"
#include "Goal_Think.h"
#include "DodgeProjectileGoal_Evalutor.h"

double DodgeProjectileGoal_Evalutor::CalculateDesirability(Raven_Bot* pBot)
{
    if (Raven_Feature::IsProjectileThreat(pBot))
        return 1.0 * m_dCharacterBias;
    return 0.0;
}

void DodgeProjectileGoal_Evalutor::SetGoal(Raven_Bot* pBot)
{
    pBot->GetBrain()->AddGoal_DodgeProjectile();
}
