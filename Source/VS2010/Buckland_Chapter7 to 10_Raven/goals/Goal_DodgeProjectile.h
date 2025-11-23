#ifndef GOAL_DODGEPROJECTILE_H
#define GOAL_DODGEPROJECTILE_H

#include "Goals/Goal_Composite.h"
#include "Raven_Goal_Types.h"
#include "../Raven_Bot.h"

class Goal_DodgeProjectile : public Goal_Composite<Raven_Bot>
{
public:
    Goal_DodgeProjectile(Raven_Bot* pOwner)
        : Goal_Composite<Raven_Bot>(pOwner, goal_dodge_projectile) {}

    void Activate();
    int Process();
    void Terminate() { m_iStatus = completed; }
};

#endif
