# Copyright (c) 2022-2025, The Isaac Lab Project Developers (https://github.com/isaac-sim/IsaacLab/blob/main/CONTRIBUTORS.md).
# All rights reserved.
#
# SPDX-License-Identifier: BSD-3-Clause

import gymnasium as gym

##
# Register Gym environments.
##

gym.register(
    id="Isaac-Velocity-Flat-T1-v0",
    entry_point="isaaclab.envs:ManagerBasedRLEnv",
    disable_env_checker=True,
    kwargs={
        "env_cfg_entry_point": f"{__name__}.flat_env_cfg:T1FlatEnvCfg",
        "rsl_rl_cfg_entry_point": f"{__name__}.rsl_rl_ppo_cfg:T1FlatPPORunnerCfg",
    },
)

gym.register(
    id="Isaac-Velocity-Flat-T1-Play-v0",
    entry_point="isaaclab.envs:ManagerBasedRLEnv",
    disable_env_checker=True,
    kwargs={
        "env_cfg_entry_point": f"{__name__}.flat_env_cfg:T1FlatEnvCfg_PLAY",
        "rsl_rl_cfg_entry_point": f"{__name__}.rsl_rl_ppo_cfg:T1FlatPPORunnerCfg",
    },
)