#include "Raven_Feature.h"
#include "Goal_DodgeProjectile.h"
#include "Goal_SeekToPosition.h"

void Goal_DodgeProjectile::Activate()
{
    m_iStatus = active;
    RemoveAllSubgoals();

    if (Raven_Feature::IsProjectileThreat(m_pOwner)) {
        Vector2D dir = Raven_Feature::DodgeDirection(m_pOwner);
        Vector2D dodgePos = m_pOwner->Pos() + dir * 80; // 옆으로 80 유닛 회피
        AddSubgoal(new Goal_SeekToPosition(m_pOwner, dodgePos));
    }
    else {
        m_iStatus = completed;
    }
}

int Goal_DodgeProjectile::Process()
{
    ActivateIfInactive();
    m_iStatus = ProcessSubgoals();
    ReactivateIfFailed();
    return m_iStatus;
}
