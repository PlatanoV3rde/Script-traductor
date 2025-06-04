

planter:
  display: '%group-color%Planter'
  description: |-
    Planta semillas en un área de 3x3
    por Shift + Click derecho.
  applies-to: ꐠ
  type: RIGHT_CLICK
  group: ULTIMATE
  settings:
    newVersionsOnly: true # Only load this enchantment if server version is 1.13 or higher
  applies:
  - ALL_HOE
  levels:
    '1':
      conditions:
      - '%player is sneaking% = true : %allow%'
      cooldown: 3
      effects:
      - PLANT_SEEDS:3
    '2':
      conditions:
      - '%player is sneaking% = true : %allow%'
      cooldown: 2
      effects:
      - PLANT_SEEDS:3
    '3':
      conditions:
      - '%player is sneaking% = true : %allow%'
      effects:
      - PLANT_SEEDS:3
strike:
  display: '%group-color%Strike'
  description: |-
    Una oportunidad de invocar un
    relampago en el oponente.
  applies-to: ꐨ
  type: SHOOT
  group: SIMPLE
  settings:
    newVersionsOnly: true # Only load this enchantment if server version is 1.13 or higher
  applies:
  - TRIDENT
  levels:
    '1':
      chance: 24
      cooldown: 3
      effects:
      - LIGHTNING @Victim
    '2':
      chance: 32
      cooldown: 3
      effects:
      - LIGHTNING @Victim
    '3':
      chance: 40
      cooldown: 4
      effects:
      - LIGHTNING @Victim
impact:
  display: '%group-color%Impact'
  description: Oportunidad de duplicar daños.
  applies-to: ꐨ
  type: SHOOT
  group: ELITE
  settings:
    newVersionsOnly: true # Only load this enchantment if server version is 1.13 or higher
  applies:
  - TRIDENT
  levels:
    '1':
      chance: 5
      cooldown: 3
      effects:
      - DOUBLE_DAMAGE @Victim
    '2':
      chance: 8
      cooldown: 3
      effects:
      - DOUBLE_DAMAGE @Victim
    '3':
      chance: 11
      cooldown: 5
      effects:
      - DOUBLE_DAMAGE @Victim
    '4':
      chance: 14
      cooldown: 6
      effects:
      - DOUBLE_DAMAGE @Victim
twinge:
  display: '%group-color%Twinge'
  description: |-
    Haz tu enemigo bleed, si
    Golpee usando un ataque cuerpo a cuerpo.
  applies-to: ꐨ
  type: ATTACK
  group: LEGENDARY
  settings:
    newVersionsOnly: true # Only load this enchantment if server version is 1.13 or higher
  applies:
  - TRIDENT
  levels:
    '1':
      chance: 5
      cooldown: 3
      effects:
      - POTION:SLOW:0:100 @Victim
      - DO_HARM:<random number>1-3</random number> @Victim
      - MESSAGE:§4Sangrando! @Victim
      - WAIT:20
      - DO_HARM:<random number>1-3</random number> @Victim
      - WAIT:20
      - DO_HARM:<random number>1-3</random number> @Victim
    '2':
      chance: 8
      cooldown: 3
      effects:
      - POTION:SLOW:0:100 @Victim
      - DO_HARM:<random number>1-3</random number> @Victim
      - MESSAGE:§4Sangrando! @Victim
      - WAIT:20
      - DO_HARM:<random number>1-3</random number> @Victim
      - WAIT:20
      - DO_HARM:<random number>1-3</random number> @Victim
    '3':
      chance: 11
      cooldown: 5
      effects:
      - POTION:SLOW:0:100 @Victim
      - DO_HARM:<random number>1-3</random number> @Victim
      - MESSAGE:§4Sangrando! @Victim
      - WAIT:20
      - DO_HARM:<random number>1-3</random number> @Victim
      - WAIT:20
      - DO_HARM:<random number>1-3</random number> @Victim
    '4':
      chance: 14
      cooldown: 6
      effects:
      - POTION:SLOW:0:100 @Victim
      - DO_HARM:<random number>1-3</random number> @Victim
      - MESSAGE:§4Sangrando! @Victim
      - WAIT:20
      - DO_HARM:<random number>1-3</random number> @Victim
      - WAIT:20
      - DO_HARM:<random number>1-3</random number> @Victim

jellylegs:
  display: '%group-color%Jelly Legs'
  description: Oportunidad de negar el daño de caída.
  applies-to: ꐥ
  type: FALL_DAMAGE
  group: ULTIMATE
  applies:
  - ALL_BOOTS
  levels:
    '1':
      chance: 40
      effects:
      - CANCEL_EVENT
      - MESSAGE:§b§l*** §f§lDAÑO DE CAIDA ANULADO §b§l***
    '2':
      chance: 80
      effects:
      - CANCEL_EVENT
      - MESSAGE:§b§l*** §f§lDAÑO DE CAIDA ANULADO §b§l***
    '3':
      effects:
      - CANCEL_EVENT
      - MESSAGE:§b§l*** §f§lDAÑO DE CAIDA ANULADO §b§l***
restore:
  display: '%group-color%Restore'
  description: |-
    Al romperse, el artículo tiene una oportunidad
    para perder este encantamiento y reparación
    la mitad de su durabilidad
  applies-to: ꐝ ꐜ ꐢ
  type: ITEM_BREAK
  group: ULTIMATE
  applies:
  - ALL_PICKAXE
  - ALL_SPADE
  - ALL_AXE
  levels:
    '1':
      chance: 40
      effects:
      - REMOVE_ENCHANT:restore
      - ADD_DURABILITY_ITEM:<round><math>-1 * (%maximum durability%/2)</math></round>
      - MESSAGE:§6§l*** §e§lOBJETO RESTAURADO §6§l***
    '2':
      chance: 60
      effects:
      - REMOVE_ENCHANT:restore
      - ADD_DURABILITY_ITEM:<round><math>-1 * (%maximum durability%/2)</math></round>
      - MESSAGE:§6§l*** §e§lOBJETO RESTAURADO §6§l***
    '3':
      chance: 80
      effects:
      - REMOVE_ENCHANT:restore
      - ADD_DURABILITY_ITEM:<round><math>-1 * (%maximum durability%/2)</math></round>
      - MESSAGE:§6§l*** §e§lOBJETO RESTAURADO §6§l***
    '4':
      chance: 100
      effects:
      - REMOVE_ENCHANT:restore
      - ADD_DURABILITY_ITEM:<round><math>-1 * (%maximum durability%/2)</math></round>
      - MESSAGE:§6§l*** §e§lOBJETO RESTAURADO §6§l***
shuffle:
  display: '%group-color%Shuffle'
  description: Baraja la barra caliente del oponente.
  applies-to: ꐤ ꐞ ꐧ ꐥ
  type: DEFENSE
  group: SIMPLE
  applies:
  - ALL_ARMOR
  levels:
    '1':
      chance: 5
      cooldown: 20
      effects:
      - SHUFFLE_HOTBAR @Attacker
    '2':
      chance: 6
      cooldown: 18
      effects:
      - SHUFFLE_HOTBAR @Attacker
    '3':
      chance: 8
      cooldown: 15
      effects:
      - SHUFFLE_HOTBAR @Attacker
aquatic:
  display: '%group-color%Aquatic'
  description: Da respiración de agua permanente.
  applies-to: ꐤ
  type: EFFECT_STATIC
  group: SIMPLE
  applies:
  - ALL_HELMET
  levels:
    '1':
      effects:
      - POTION:WATER_BREATHING:0
autosmelt:
  display: '%group-color%Auto Smelt'
  description: |-
    Los minerales se funden automáticamente
    Cuando se extrae.
  applies-to: ꐢ
  type: MINING
  group: SIMPLE
  applies:
  - ALL_PICKAXE
  levels:
    '1':
      chance: 41
      effects:
      - SMELT
    '2':
      chance: 62
      effects:
      - SMELT
    '3':
      chance: 100
      effects:
      - SMELT
confusion:
  display: '%group-color%Confusion'
  description: |-
    Una oportunidad para aplicar el efecto de náuseas
    a tu víctima.
  applies-to: ꐝ
  type: ATTACK
  group: SIMPLE
  applies:
  - ALL_AXE
  levels:
    '1':
      chance: 13
      cooldown: 4
      effects:
      - POTION:CONFUSION:0:40 @Victim
    '2':
      chance: 19
      cooldown: 5
      effects:
      - POTION:CONFUSION:0:80 @Victim
    '3':
      chance: 24
      cooldown: 6
      effects:
      - POTION:CONFUSION:0:120 @Victim
etheral:
  display: '%group-color%Etheral'
  description: Ganar haste al matar a los monstruos
  applies-to: ꐚ
  type: KILL_MOB
  group: SIMPLE
  applies:
  - ALL_SWORD
  levels:
    '1':
      effects:
      - POTION:FAST_DIGGING:0:80
    '2':
      effects:
      - POTION:FAST_DIGGING:1:80
    '3':
      effects:
      - POTION:FAST_DIGGING:2:80
experience:
  display: '%group-color%Experience'
  description: Oportunidad de obtener experience de la minería.
  applies-to: ꐝ ꐜ ꐢ
  type: MINING
  group: SIMPLE
  applies:
  - ALL_PICKAXE
  - ALL_SPADE
  - ALL_AXE
  levels:
    '1':
      chance: 15
      cooldown: 1
      effects:
      - EXP:<random number>2-5</random number>
    '2':
      chance: 30
      cooldown: 1
      effects:
      - EXP:<random number>2-5</random number>
    '3':
      chance: 45
      cooldown: 1
      effects:
      - EXP:<random number>2-5</random number>
    '4':
      chance: 60
      cooldown: 1
      effects:
      - EXP:<random number>2-5</random number>
    '5':
      chance: 75
      cooldown: 1
      effects:
      - EXP:<random number>2-5</random number>
haste:
  display: '%group-color%Haste'
  description: Te permite balancear tus herramientas más rápido.
  applies-to: ꐝ ꐜ ꐢ
  type: HELD
  group: SIMPLE
  applies:
  - ALL_PICKAXE
  - ALL_SPADE
  - ALL_AXE
  levels:
    '1':
      effects:
      - POTION:FAST_DIGGING:0
    '2':
      effects:
      - POTION:FAST_DIGGING:1
    '3':
      effects:
      - POTION:FAST_DIGGING:2
insomnia:
  display: '%group-color%Insomnia'
  description: |-
    Da la lentitud y el balanceo lento
    y confusion.
  applies-to: ꐚ
  type: ATTACK;ATTACK_MOB
  group: SIMPLE
  applies:
  - ALL_SWORD
  levels:
    '1':
      chance: 10
      cooldown: 10
      effects:
      - POTION:SLOW:0:40 @Victim
      - POTION:CONFUSION:0:40 @Victim
      - POTION:SLOW_DIGGING:0:60 @Victim
    '2':
      chance: 12
      cooldown: 10
      effects:
      - POTION:SLOW:0:80 @Victim
      - POTION:CONFUSION:0:80 @Victim
      - POTION:SLOW_DIGGING:0:100 @Victim
    '3':
      chance: 14
      cooldown: 10
      effects:
      - POTION:SLOW:1:100 @Victim
      - POTION:CONFUSION:1:100 @Victim
      - POTION:SLOW_DIGGING:1:120 @Victim
    '4':
      chance: 16
      cooldown: 9
      effects:
      - POTION:SLOW:1:120 @Victim
      - POTION:CONFUSION:1:120 @Victim
      - POTION:SLOW_DIGGING:1:140 @Victim
    '5':
      chance: 18
      cooldown: 9
      effects:
      - POTION:SLOW:1:140 @Victim
      - POTION:CONFUSION:1:140 @Victim
      - POTION:SLOW_DIGGING:1:160 @Victim
    '6':
      chance: 20
      cooldown: 8
      effects:
      - POTION:SLOW:1:180 @Victim
      - POTION:CONFUSION:1:180 @Victim
      - POTION:SLOW_DIGGING:1:200 @Victim
    '7':
      chance: 22
      cooldown: 8
      effects:
      - POTION:SLOW:2:80 @Victim
      - POTION:CONFUSION:2:80 @Victim
      - POTION:SLOW_DIGGING:2:100 @Victim
lightning:
  display: '%group-color%Lightning'
  description: |-
    Una oportunidad de invocar un
    rayo en el oponente.
  applies-to: ꐣ
  type: SHOOT;SHOOT_MOB
  group: SIMPLE
  applies:
  - BOW
  - CROSSBOW
  levels:
    '1':
      chance: 24
      cooldown: 3
      effects:
      - LIGHTNING @Victim
    '2':
      chance: 32
      cooldown: 3
      effects:
      - LIGHTNING @Victim
    '3':
      chance: 40
      cooldown: 3
      effects:
      - LIGHTNING @Victim
oxygenate:
  display: '%group-color%Oxygenate'
  description: |-
    Rellena los niveles de oxígeno cuando
    Bloques de ruptura bajo el agua.
  applies-to: ꐢ
  type: MINING
  group: SIMPLE
  applies:
  - ALL_PICKAXE
  levels:
    '1':
      cooldown: 3
      effects:
      - AIR
thunderingblow:
  display: '%group-color%Thundering Blow'
  description: Puede causar un efecto de smite en tu enemigo.
  applies-to: ꐚ
  type: ATTACK;ATTACK_MOB
  group: SIMPLE
  applies:
  - ALL_SWORD
  levels:
    '1':
      chance: 12
      cooldown: 6
      effects:
      - LIGHTNING @Victim
    '2':
      chance: 17
      cooldown: 4
      effects:
      - LIGHTNING @Victim
    '3':
      chance: 24
      cooldown: 3
      effects:
      - LIGHTNING @Victim
glowing:
  display: '%group-color%Glowing'
  description: Da visión nocturna permanente.
  applies-to: ꐤ
  type: EFFECT_STATIC
  group: SIMPLE
  applies:
  - ALL_HELMET
  levels:
    '1':
      effects:
      - POTION:NIGHT_VISION:0
decapitation:
  display: '%group-color%Decapitation'
  description: |-
    Las víctimas tienen la oportunidad de dejar caer
    su cabeza en la muerte.
  applies-to: ꐝ
  type: KILL_PLAYER
  group: SIMPLE
  applies:
  - ALL_AXE
  levels:
    '1':
      chance: 20
      effects:
      - DROP_HEAD @Victim
    '2':
      chance: 40
      effects:
      - DROP_HEAD @Victim
    '3':
      chance: 60
      effects:
      - DROP_HEAD @Victim
headless:
  display: '%group-color%Headless'
  description: |-
    Las víctimas tienen la oportunidad de dejar caer
    su cabeza en la muerte.
  applies-to: ꐚ
  type: KILL_PLAYER
  group: SIMPLE
  applies:
  - ALL_SWORD
  levels:
    '1':
      chance: 20
      effects:
      - DROP_HEAD @Victim
    '2':
      chance: 40
      effects:
      - DROP_HEAD @Victim
    '3':
      chance: 60
      effects:
      - DROP_HEAD @Victim
obliterate:
  display: '%group-color%Obliterate'
  description: Backback extremo.
  applies-to: ꐚ
  type: ATTACK;ATTACK_MOB
  group: SIMPLE
  applies:
  - ALL_SWORD
  levels:
    '1':
      chance: 30
      cooldown: 12
      effects:
      - PULL_AWAY:1.0 @Victim
    '2':
      chance: 36
      cooldown: 12
      effects:
      - PULL_AWAY:1.5 @Victim
    '3':
      chance: 42
      cooldown: 12
      effects:
      - PULL_AWAY:2.0 @Victim
    '4':
      chance: 48
      cooldown: 13
      effects:
      - PULL_AWAY:2.5 @Victim
    '5':
      chance: 54
      cooldown: 13
      effects:
      - PULL_AWAY:3.0 @Victim
epicness:
  display: '%group-color%Epicness'
  description: Da partículas y efectos de sonido.
  applies-to: ꐚ
  type: ATTACK;ATTACK_MOB
  group: SIMPLE
  applies:
  - ALL_SWORD
  levels:
    '1':
      chance: 20
      cooldown: 3
      effects:
      - PARTICLE:LARGE_SMOKE:50:1 @Victim
      - PLAY_SOUND:GHAST_SCREAM
    '2':
      chance: 40
      cooldown: 3
      effects:
      - PARTICLE:LARGE_SMOKE:50:1 @Victim
      - PLAY_SOUND:GHAST_SCREAM
    '3':
      chance: 60
      cooldown: 3
      effects:
      - PARTICLE:LARGE_SMOKE:50:1 @Victim
      - PLAY_SOUND:GHAST_SCREAM
lifebloom:
  display: '%group-color%Lifebloom'
  description: |-
    Cura completamente los aliados
    y truces en tu muerte
    en 10 block radio.
  applies-to: ꐞ
  type: DEATH
  group: UNIQUE
  applies:
  - ALL_LEGGINGS
  levels:
    '1':
      chance: 20
      cooldown: 10
      effects:
      - ADD_HEALTH:40 @Aoe{r=10,t=undamageable}
      - MESSAGE:§e§l*** §eLifebloom §e§l*** §7(%victim name%) @Aoe{r=10,t=undamageable}
    '2':
      chance: 30
      cooldown: 10
      effects:
      - ADD_HEALTH:40 @Aoe{r=10,t=undamageable}
      - MESSAGE:§e§l*** §eLifebloom §e§l*** §7(%victim name%) @Aoe{r=10,t=undamageable}
    '3':
      chance: 40
      cooldown: 10
      effects:
      - ADD_HEALTH:40 @Aoe{r=10,t=undamageable}
      - MESSAGE:§e§l*** §eLifebloom §e§l*** §7(%victim name%) @Aoe{r=10,t=undamageable}
    '4':
      chance: 50
      cooldown: 15
      effects:
      - ADD_HEALTH:40 @Aoe{r=10,t=undamageable}
      - MESSAGE:§e§l*** §eLifebloom §e§l*** §7(%victim name%) @Aoe{r=10,t=undamageable}
    '5':
      chance: 50
      cooldown: 15
      effects:
      - ADD_HEALTH:40 @Aoe{r=10,t=undamageable}
      - MESSAGE:§e§l*** §eLifebloom §e§l*** §7(%victim name%) @Aoe{r=10,t=undamageable}
famine:
  display: '%group-color%Famine'
  description: Una oportunidad de darle a tu oponente el efecto del hambre.
  applies-to: ꐚ ꐝ
  type: ATTACK
  group: UNIQUE
  applies:
  - ALL_SWORD
  - ALL_AXE
  levels:
    '1':
      chance: 12
      cooldown: 8
      effects:
      - POTION:HUNGER:0:80 @Victim
    '2':
      chance: 15
      cooldown: 8
      effects:
      - POTION:HUNGER:0:120 @Victim
    '3':
      chance: 18
      cooldown: 8
      effects:
      - POTION:HUNGER:1:80 @Victim
    '4':
      chance: 22
      cooldown: 8
      effects:
      - POTION:HUNGER:1:120 @Victim
obsidiandestroyer:
  display: '%group-color%Obsidian Destroyer'
  description: Oportunidad de romper instantáneamente los bloques de obsidiana.
  applies-to: ꐢ
  type: SWING
  group: UNIQUE
  applies:
  - ALL_PICKAXE
  levels:
    '1':
      chance: 15
      cooldown: 8
      conditions:
      - '%block type% != OBSIDIAN : %stop%'
      - '%can break% = true : %allow%'
      effects:
      - BREAK_BLOCK
    '2':
      chance: 30
      cooldown: 6
      conditions:
      - '%block type% != OBSIDIAN : %stop%'
      - '%can break% = true : %allow%'
      effects:
      - BREAK_BLOCK
    '3':
      chance: 50
      cooldown: 5
      conditions:
      - '%block type% != OBSIDIAN : %stop%'
      - '%can break% = true : %allow%'
      effects:
      - BREAK_BLOCK
    '4':
      chance: 65
      cooldown: 4
      conditions:
      - '%block type% != OBSIDIAN : %stop%'
      - '%can break% = true : %allow%'
      effects:
      - BREAK_BLOCK
    '5':
      chance: 80
      cooldown: 3
      conditions:
      - '%block type% != OBSIDIAN : %stop%'
      - '%can break% = true : %allow%'
      effects:
      - BREAK_BLOCK
berserk:
  display: '%group-color%Berserk'
  description: |-
    Una oportunidad de fuerza
    y fatiga minera.
  applies-to: ꐝ
  type: ATTACK;ATTACK_MOB
  group: UNIQUE
  applies:
  - ALL_AXE
  levels:
    '1':
      chance: 4
      cooldown: 8
      effects:
      - POTION:SLOW_DIGGING:0:60 @Attacker
      - POTION:INCREASE_DAMAGE:0:60 @Attacker
    '2':
      chance: 8
      cooldown: 7
      effects:
      - POTION:SLOW_DIGGING:0:80 @Attacker
      - POTION:INCREASE_DAMAGE:0:80 @Attacker
    '3':
      chance: 12
      cooldown: 6
      effects:
      - POTION:SLOW_DIGGING:0:100 @Attacker
      - POTION:INCREASE_DAMAGE:0:100 @Attacker
    '4':
      chance: 16
      cooldown: 5
      effects:
      - POTION:SLOW_DIGGING:1:80 @Attacker
      - POTION:INCREASE_DAMAGE:1:80 @Attacker
    '5':
      chance: 20
      cooldown: 4
      effects:
      - POTION:SLOW_DIGGING:1:100 @Attacker
      - POTION:INCREASE_DAMAGE:1:100 @Attacker
ward:
  display: '%group-color%Ward'
  description: |-
    Una oportunidad de absorber enemigo
    dañar y curarte
  applies-to: ꐤ ꐞ ꐧ ꐥ
  type: DEFENSE;DEFENSE_MOB
  group: UNIQUE
  applies:
  - ALL_ARMOR
  levels:
    '1':
      chance: 3
      cooldown: 5
      effects:
      - CANCEL_EVENT
      - POTION:ABSORPTION:0:80 @Victim
    '2':
      chance: 7
      cooldown: 5
      effects:
      - CANCEL_EVENT
      - POTION:ABSORPTION:0:80 @Victim
    '3':
      chance: 11
      cooldown: 5
      effects:
      - CANCEL_EVENT
      - POTION:ABSORPTION:0:80 @Victim
    '4':
      chance: 15
      cooldown: 5
      effects:
      - CANCEL_EVENT
      - POTION:ABSORPTION:0:80 @Victim
curse:
  display: '%group-color%Curse'
  description: Da resistencia, lentitud y resistencia a bajo HP.
  applies-to: ꐧ
  type: DEFENSE;DEFENSE_MOB
  group: UNIQUE
  applies:
  - ALL_CHESTPLATE
  levels:
    '1':
      chance: 10
      cooldown: 7
      conditions:
      - '%victim health% > 10 : %stop%'
      effects:
      - POTION:SLOW_DIGGING:0:100 @Attacker
      - POTION:INCREASE_DAMAGE:0:40 @Victim
      - POTION:DAMAGE_RESISTANCE:0:40 @Victim
    '2':
      chance: 12
      cooldown: 7
      conditions:
      - '%victim health% > 10 : %stop%'
      effects:
      - POTION:SLOW_DIGGING:0:120 @Attacker
      - POTION:INCREASE_DAMAGE:0:60 @Victim
      - POTION:DAMAGE_RESISTANCE:0:60 @Victim
    '3':
      chance: 14
      cooldown: 7
      conditions:
      - '%victim health% > 10 : %stop%'
      effects:
      - POTION:SLOW_DIGGING:1:80 @Attacker
      - POTION:INCREASE_DAMAGE:0:80 @Victim
      - POTION:DAMAGE_RESISTANCE:0:80 @Victim
    '4':
      chance: 16
      cooldown: 7
      conditions:
      - '%victim health% > 10 : %stop%'
      effects:
      - POTION:SLOW_DIGGING:1:100 @Attacker
      - POTION:INCREASE_DAMAGE:1:60 @Victim
      - POTION:DAMAGE_RESISTANCE:1:60 @Victim
    '5':
      chance: 18
      cooldown: 7
      conditions:
      - '%victim health% > 10 : %stop%'
      effects:
      - POTION:SLOW_DIGGING:2:100 @Attacker
      - POTION:INCREASE_DAMAGE:1:80 @Victim
      - POTION:DAMAGE_RESISTANCE:1:80 @Victim
endershift:
  display: '%group-color%EnderShift'
  description: Da un impulso de velocidad/salud a bajo HP.
  applies-to: Helmet, Boots
  type: DEFENSE
  group: UNIQUE
  applies:
  - ALL_HELMET
  - ALL_BOOTS
  levels:
    '1':
      chance: 16
      cooldown: 6
      conditions:
      - '%victim health% > 6 : %stop%'
      effects:
      - POTION:SPEED:1:120 @Victim
      - MESSAGE:§dYou were about to die, so you have entered the Ender Dimension!
      - POTION:ABSORPTION:0:80 @Victim
    '2':
      chance: 17
      cooldown: 8
      conditions:
      - '%victim health% > 6 : %stop%'
      effects:
      - POTION:SPEED:1:120 @Victim
      - MESSAGE:§dYou were about to die, so you have entered the Ender Dimension!
      - POTION:ABSORPTION:1:80 @Victim
    '3':
      chance: 18
      cooldown: 12
      conditions:
      - '%victim health% > 6 : %stop%'
      effects:
      - POTION:SPEED:1:120 @Victim
      - MESSAGE:§dYou were about to die, so you have entered the Ender Dimension!
      - POTION:ABSORPTION:2:80 @Victim
explosive:
  display: '%group-color%Explosive'
  description: Flechas explosivas.
  applies-to: ꐣ
  type: SHOOT;SHOOT_MOB
  group: UNIQUE
  applies:
  - BOW
  - CROSSBOW
  levels:
    '1':
      chance: 20
      cooldown: 7
      effects:
      - TNT @Victim
    '2':
      chance: 30
      cooldown: 8
      effects:
      - TNT @Victim
    '3':
      chance: 40
      cooldown: 8
      effects:
      - TNT @Victim
    '4':
      chance: 50
      cooldown: 8
      effects:
      - TNT @Victim
    '5':
      chance: 60
      cooldown: 9
      effects:
      - TNT @Victim
featherweight:
  display: '%group-color%Featherweight'
  description: Una oportunidad de dar una explosión de haste.
  applies-to: ꐚ
  type: ATTACK;ATTACK_MOB
  group: UNIQUE
  applies:
  - ALL_SWORD
  levels:
    '1':
      chance: 35
      cooldown: 2
      effects:
      - POTION:FAST_DIGGING:0:60
    '2':
      chance: 55
      cooldown: 2
      effects:
      - POTION:FAST_DIGGING:1:80
    '3':
      chance: 75
      cooldown: 2
      effects:
      - POTION:FAST_DIGGING:2:100
molten:
  display: '%group-color%Molten'
  description: Posibilidad de poner a tu atacante en llamas.
  applies-to: ꐤ ꐞ ꐧ ꐥ
  type: DEFENSE;DEFENSE_MOB
  group: UNIQUE
  applies:
  - ALL_ARMOR
  levels:
    '1':
      chance: 21
      cooldown: 2
      effects:
      - BURN:2 @Attacker
    '2':
      chance: 32
      cooldown: 2
      effects:
      - BURN:4 @Attacker
    '3':
      chance: 49
      cooldown: 2
      effects:
      - BURN:6 @Attacker
    '4':
      chance: 63
      cooldown: 2
      effects:
      - BURN:8 @Attacker
ravenous:
  display: '%group-color%Ravenous'
  description: |-
    Oportunidad de recuperar el hambre
    mientras está en combate.
  applies-to: ꐝ
  type: ATTACK;ATTACK_MOB
  group: UNIQUE
  applies:
  - ALL_AXE
  levels:
    '1':
      chance: 14
      cooldown: 2
      effects:
      - ADD_FOOD:<random number>1-4</random number> @Attacker
    '2':
      chance: 18
      cooldown: 2
      effects:
      - ADD_FOOD:<random number>1-4</random number> @Attacker
    '3':
      chance: 22
      cooldown: 2
      effects:
      - ADD_FOOD:<random number>1-4</random number> @Attacker
    '4':
      chance: 26
      cooldown: 2
      effects:
      - ADD_FOOD:<random number>1-4</random number> @Attacker
commander:
  display: '%group-color%Commander'
  description: Nearby allies are given haste.
  applies-to: ꐤ ꐞ ꐧ ꐥ
  type: DEFENSE
  group: UNIQUE
  applies:
  - ALL_ARMOR
  levels:
    '1':
      chance: 6
      cooldown: 6
      effects:
      - POTION:HASTE:0:140 @Aoe{r=5,t=undamageable}
    '2':
      chance: 9
      cooldown: 6
      effects:
      - POTION:HASTE:0:140 @Aoe{r=5,t=undamageable}
    '3':
      chance: 12
      cooldown: 6
      effects:
      - POTION:HASTE:0:140 @Aoe{r=5,t=undamageable}
    '4':
      chance: 15
      cooldown: 6
      effects:
      - POTION:HASTE:0:140 @Aoe{r=5,t=undamageable}
    '5':
      chance: 18
      cooldown: 6
      effects:
      - POTION:HASTE:0:140 @Aoe{r=5,t=undamageable}
selfdestruct:
  display: '%group-color%Self Destruct'
  description: |-
    Cuando cerca de la muerte,
    TNT genera a tu alrededor para
    terminar con usted y quitarse la caída
    elementos.
  applies-to: ꐤ ꐞ ꐧ ꐥ
  type: DEFENSE
  group: UNIQUE
  applies:
  - ALL_ARMOR
  levels:
    '1':
      chance: 23
      cooldown: 4
      conditions: '%victim health% > 3 : %stop%'
      effects:
      - MESSAGE:§c§l*** SelfDestruct ***
      - TNT @Victim
    '2':
      chance: 35
      cooldown: 4
      conditions: '%victim health% > 3 : %stop%'
      effects:
      - MESSAGE:§c§l*** SelfDestruct ***
      - TNT @Victim
    '3':
      chance: 42
      cooldown: 4
      conditions: '%victim health% > 3 : %stop%'
      effects:
      - MESSAGE:§c§l*** SelfDestruct ***
      - TNT @Victim
telepathy:
  display: '%group-color%Telepathy'
  description: |-
    Coloca automáticamente bloques rotos
    por herramientas en su inventario.
  applies-to: ꐝ ꐜ ꐢ
  type: MINING
  group: UNIQUE
  applies:
  - ALL_PICKAXE
  - ALL_SPADE
  - ALL_AXE
  levels:
    '1':
      chance: 40
      effects:
      - TP_DROPS
    '2':
      chance: 60
      effects:
      - TP_DROPS
    '3':
      chance: 80
      effects:
      - TP_DROPS
    '4':
      effects:
      - TP_DROPS
sustain:
  display: '%group-color%Sustain'
  description: Oportunidad de recuperar el hambre al ser golpeado.
  applies-to: ꐤ ꐞ ꐧ ꐥ
  type: DEFENSE;DEFENSE_MOB;DEFENSE_PROJECTILE
  group: UNIQUE
  applies:
  - ALL_ARMOR
  levels:
    '1':
      chance: 12
      cooldown: 8
      effects:
      - ADD_FOOD:<random number>1-4</random number> @Victim
    '2':
      chance: 14
      cooldown: 8
      effects:
      - ADD_FOOD:<random number>1-4</random number> @Victim
    '3':
      chance: 16
      cooldown: 8
      effects:
      - ADD_FOOD:<random number>1-4</random number> @Victim
    '4':
      chance: 20
      cooldown: 8
      effects:
      - ADD_FOOD:<random number>1-4</random number> @Victim
skillswipe:
  display: '%group-color%Skill Swipe'
  description: |-
    Una oportunidad de robar algunos de tus enemigos
    EXP cada vez que los dañas.
  applies-to: ꐚ
  type: ATTACK
  group: UNIQUE
  applies:
  - ALL_SWORD
  levels:
    '1':
      chance: 15
      cooldown: 5
      effects:
      - STEAL_EXP:<random number>25-125</random number> @Attacker
    '2':
      chance: 17
      cooldown: 5
      effects:
      - STEAL_EXP:<random number>25-175</random number> @Attacker
    '3':
      chance: 19
      cooldown: 5
      effects:
      - STEAL_EXP:<random number>25-225</random number> @Attacker
    '4':
      chance: 21
      cooldown: 5
      effects:
      - STEAL_EXP:<random number>25-275</random number> @Attacker
    '5':
      chance: 23
      cooldown: 5
      effects:
      - STEAL_EXP:<random number>25-350</random number> @Attacker
plaguecarrier:
  display: '%group-color%Plague Carrier'
  description: |-
    Cuando cerca de la muerte, convocaciones de enredaderas
    y debuffs para vengarte.
  applies-to: ꐞ
  type: DEFENSE;DEFENSE_MOB
  group: UNIQUE
  applies:
  - ALL_LEGGINGS
  levels:
    '1':
      chance: 13
      cooldown: 3
      conditions:
      - '%victim health% > 4 : %stop%'
      effects:
      - GUARD:CREEPER:@Victim
      - POTION:BLINDNESS:0:40 @Attacker
    '2':
      chance: 17
      cooldown: 3
      conditions:
      - '%victim health% > 4 : %stop%'
      effects:
      - GUARD:CREEPER:@Victim
      - POTION:BLINDNESS:0:60 @Attacker
    '3':
      chance: 24
      cooldown: 3
      conditions:
      - '%victim health% > 4 : %stop%'
      effects:
      - GUARD:CREEPER:@Victim
      - POTION:BLINDNESS:0:100 @Attacker
    '4':
      chance: 30
      cooldown: 3
      conditions:
      - '%victim health% > 4 : %stop%'
      effects:
      - GUARD:CREEPER:@Victim
      - POTION:BLINDNESS:1:40 @Attacker
    '5':
      chance: 38
      cooldown: 3
      conditions:
      - '%victim health% > 4 : %stop%'
      effects:
      - GUARD:CREEPER:@Victim
      - GUARD:CREEPER:@Victim
      - POTION:BLINDNESS:1:80 @Attacker
    '6':
      chance: 46
      cooldown: 3
      conditions:
      - '%victim health% > 4 : %stop%'
      effects:
      - GUARD:CREEPER:@Victim
      - GUARD:CREEPER:@Victim
      - POTION:BLINDNESS:1:120 @Attacker
    '7':
      chance: 55
      cooldown: 3
      conditions:
      - '%victim health% > 4 : %stop%'
      effects:
      - GUARD:CREEPER:@Victim
      - GUARD:CREEPER:@Victim
      - POTION:BLINDNESS:2:60 @Attacker
    '8':
      chance: 69
      cooldown: 3
      conditions:
      - '%victim health% > 4 : %stop%'
      effects:
      - GUARD:CREEPER:@Victim
      - GUARD:CREEPER:@Victim
      - GUARD:CREEPER:@Victim
      - POTION:BLINDNESS:2:100 @Attacker
virus:
  display: '%group-color%Virus'
  description: |-
    Multiplica todos los efectos de marchitar y veneno en el
    objetivo afectado.
  applies-to: ꐣ
  type: SHOOT
  group: UNIQUE
  applies:
  - BOW
  - CROSSBOW
  levels:
    '1':
      chance: 12
      cooldown: 3
      conditions:
      - '%victim has potion effect WITHER% != TRUE : %stop%'
      - '%victim has potion effect POISON% != TRUE : %stop%'
      effects:
      - POTION:WITHER:2:60 @Victim
      - POTION:POISON:2:60 @Victim
    '2':
      chance: 16
      cooldown: 3
      conditions:
      - '%victim has potion effect WITHER% != TRUE : %stop%'
      - '%victim has potion effect POISON% != TRUE : %stop%'
      effects:
      - POTION:WITHER:2:60 @Victim
      - POTION:POISON:2:60 @Victim
    '3':
      chance: 20
      cooldown: 3
      conditions:
      - '%victim has potion effect WITHER% != TRUE : %stop%'
      - '%victim has potion effect POISON% != TRUE : %stop%'
      effects:
      - POTION:WITHER:2:60 @Victim
      - POTION:POISON:2:60 @Victim
    '4':
      chance: 24
      cooldown: 3
      conditions:
      - '%victim has potion effect WITHER% != TRUE : %stop%'
      - '%victim has potion effect POISON% != TRUE : %stop%'
      effects:
      - POTION:WITHER:2:60 @Victim
      - POTION:POISON:2:60 @Victim
antigravity:
  display: '%group-color%Anti Gravity'
  description: Super Jump.
  applies-to: ꐥ
  type: EFFECT_STATIC
  group: ELITE
  applies:
  - ALL_BOOTS
  levels:
    '1':
      effects:
      - POTION:JUMP:2
    '2':
      effects:
      - POTION:JUMP:3
    '3':
      effects:
      - POTION:JUMP:4
enderslayer:
  display: '%group-color%Ender Slayer'
  description: Aumenta el daño tratado a los dragones enderman y ender.
  applies-to: ꐚ ꐝ
  type: ATTACK_MOB
  group: ELITE
  applies:
  - ALL_SWORD
  - ALL_AXE
  levels:
    '1':
      chance: 16
      cooldown: 2
      conditions:
      - '%mob type% = ENDERMAN or %mob type% = ENDER_DRAGON or %mob type% = ENDERDRAGON
        : %allow%'
      effects:
      - INCREASE_DAMAGE:<random number>10-40</random number> @Attacker
    '2':
      chance: 21
      cooldown: 2
      conditions:
      - '%mob type% = ENDERMAN or %mob type% = ENDER_DRAGON or %mob type% = ENDERDRAGON
        : %allow%'
      effects:
      - INCREASE_DAMAGE:<random number>10-40</random number> @Attacker
    '3':
      chance: 29
      cooldown: 2
      conditions:
      - '%mob type% = ENDERMAN or %mob type% = ENDER_DRAGON or %mob type% = ENDERDRAGON
        : %allow%'
      effects:
      - INCREASE_DAMAGE:<random number>10-40</random number> @Attacker
    '4':
      chance: 34
      cooldown: 2
      conditions:
      - '%mob type% = ENDERMAN or %mob type% = ENDER_DRAGON or %mob type% = ENDERDRAGON
        : %allow%'
      effects:
      - INCREASE_DAMAGE:<random number>10-40</random number> @Attacker
    '5':
      chance: 41
      cooldown: 2
      conditions:
      - '%mob type% = ENDERMAN or %mob type% = ENDER_DRAGON or %mob type% = ENDERDRAGON
        : %allow%'
      effects:
      - INCREASE_DAMAGE:<random number>10-40</random number> @Attacker
reaper:
  display: '%group-color%Reaper'
  description: |-
    Una oportunidad de darle a tu oponente el
    Efectos de marchitamiento y ceguera
    Mientras se da daño
  applies-to: ꐝ
  type: ATTACK
  group: ELITE
  applies:
  - ALL_AXE
  levels:
    '1':
      chance: 8
      cooldown: 16
      effects:
      - POTION:WITHER:0:120 @Victim
      - POTION:BLINDNESS:0:120 @Victim
      - MESSAGE:§c§l** REAPER ** @Victim
    '2':
      chance: 10
      cooldown: 14
      effects:
      - POTION:WITHER:0:120 @Victim
      - POTION:BLINDNESS:0:120 @Victim
      - MESSAGE:§c§l** REAPER ** @Victim
    '3':
      chance: 12
      cooldown: 12
      effects:
      - POTION:WITHER:0:120 @Victim
      - POTION:BLINDNESS:0:120 @Victim
      - MESSAGE:§c§l** REAPER ** @Victim
    '4':
      chance: 14
      cooldown: 10
      effects:
      - POTION:WITHER:0:120 @Victim
      - POTION:BLINDNESS:0:120 @Victim
      - MESSAGE:§c§l** REAPER ** @Victim
netherslayer:
  display: '%group-color%Nether Slayer'
  description: Aumenta el daño tratado a las llamas y los pigmen zombie.
  applies-to: ꐚ ꐝ
  type: ATTACK_MOB
  group: ELITE
  applies:
  - ALL_SWORD
  - ALL_AXE
  levels:
    '1':
      chance: 16
      cooldown: 2
      conditions:
      - '%mob type% = BLAZE or %mob type% = ZOMBIE_PIGMAN or %mob type% = PIG_ZOMBIE
        : %allow%'
      effects:
      - INCREASE_DAMAGE:<random number>10-40</random number> @Attacker
    '2':
      chance: 21
      cooldown: 2
      conditions:
      - '%mob type% = BLAZE or %mob type% = ZOMBIE_PIGMAN or %mob type% = PIG_ZOMBIE
        : %allow%'
      effects:
      - INCREASE_DAMAGE:<random number>10-40</random number> @Attacker
    '3':
      chance: 29
      cooldown: 2
      conditions:
      - '%mob type% = BLAZE or %mob type% = ZOMBIE_PIGMAN or %mob type% = PIG_ZOMBIE
        : %allow%'
      effects:
      - INCREASE_DAMAGE:<random number>10-40</random number> @Attacker
    '4':
      chance: 34
      cooldown: 2
      conditions:
      - '%mob type% = BLAZE or %mob type% = ZOMBIE_PIGMAN or %mob type% = PIG_ZOMBIE
        : %allow%'
      effects:
      - INCREASE_DAMAGE:<random number>10-40</random number> @Attacker
    '5':
      chance: 41
      cooldown: 2
      conditions:
      - '%mob type% = BLAZE or %mob type% = ZOMBIE_PIGMAN or %mob type% = PIG_ZOMBIE
        : %allow%'
      effects:
      - INCREASE_DAMAGE:<random number>10-40</random number> @Attacker
blind:
  display: '%group-color%Blind'
  description: |-
    Una posibilidad de causar ceguera
    Al atacar.
  applies-to: ꐚ
  type: ATTACK
  group: ELITE
  applies:
  - ALL_SWORD
  levels:
    '1':
      chance: 17
      cooldown: 3
      effects:
      - POTION:BLINDNESS:0:60 @Victim
    '2':
      chance: 25
      cooldown: 3
      effects:
      - POTION:BLINDNESS:1:80 @Victim
    '3':
      chance: 33
      cooldown: 3
      effects:
      - POTION:BLINDNESS:2:100 @Victim
shackle:
  display: '%group-color%Shackle'
  description: Tu ataque tira de la mafia hacia ti.
  applies-to: ꐚ
  type: ATTACK_MOB
  group: ELITE
  applies:
  - ALL_SWORD
  levels:
    '1':
      chance: 30
      effects:
      - PULL_CLOSER:0.1 @Victim
    '2':
      chance: 60
      effects:
      - PULL_CLOSER:0.1 @Victim
    '3':
      effects:
      - PULL_CLOSER:0.1 @Victim
cactus:
  display: '%group-color%Cactus'
  description: |-
    Lesiona a tu atacante pero no
    afectar su durabilidad.
  applies-to: ꐤ ꐞ ꐧ ꐥ
  type: DEFENSE
  group: ELITE
  applies:
  - ALL_ARMOR
  levels:
    '1':
      chance: 18
      cooldown: 7
      effects:
      - CANCEL_EVENT
      - DO_HARM:<random number>1-2</random number> @Attacker
    '2':
      chance: 23
      cooldown: 7
      effects:
      - CANCEL_EVENT
      - DO_HARM:<random number>1-3</random number> @Attacker
execute:
  display: '%group-color%Execute'
  description: |-
    Dañar a Buff cuando su objetivo está en
    bajo HP.
  applies-to: ꐚ
  type: ATTACK;ATTACK_MOB
  group: ELITE
  applies:
  - ALL_SWORD
  levels:
    '1':
      chance: 9
      cooldown: 2
      conditions:
      - '%victim health% > 6 : %stop%'
      effects:
      - INCREASE_DAMAGE:<random number>10-50</random number> @Attacker
      - MESSAGE:§b§l** EXECUTE ** @Attacker
    '2':
      chance: 15
      cooldown: 2
      conditions:
      - '%victim health% > 6 : %stop%'
      effects:
      - INCREASE_DAMAGE:<random number>10-50</random number> @Attacker
      - MESSAGE:§b§l** EXECUTE ** @Attacker
    '3':
      chance: 19
      cooldown: 2
      conditions:
      - '%victim health% > 6 : %stop%'
      effects:
      - INCREASE_DAMAGE:<random number>10-50</random number> @Attacker
      - MESSAGE:§b§l** EXECUTE ** @Attacker
    '4':
      chance: 24
      cooldown: 2
      conditions:
      - '%victim health% > 6 : %stop%'
      effects:
      - INCREASE_DAMAGE:<random number>10-50</random number> @Attacker
      - MESSAGE:§b§l** EXECUTE ** @Attacker
    '5':
      chance: 29
      cooldown: 2
      conditions:
      - '%victim health% > 6 : %stop%'
      effects:
      - INCREASE_DAMAGE:<random number>10-50</random number> @Attacker
      - MESSAGE:§b§l** EXECUTE ** @Attacker
    '6':
      chance: 32
      cooldown: 2
      conditions:
      - '%victim health% > 6 : %stop%'
      effects:
      - INCREASE_DAMAGE:<random number>10-50</random number> @Attacker
      - MESSAGE:§b§l** EXECUTE ** @Attacker
    '7':
      chance: 40
      cooldown: 2
      conditions:
      - '%victim health% > 6 : %stop%'
      effects:
      - INCREASE_DAMAGE:<random number>10-50</random number> @Attacker
      - MESSAGE:§b§l** EXECUTE ** @Attacker
frozen:
  display: '%group-color%Frozen'
  description: |-
    Puede causar la lentitud al atacante
    Al defender.
  applies-to: ꐤ ꐞ ꐧ ꐥ
  type: DEFENSE;DEFENSE_MOB
  group: ELITE
  applies:
  - ALL_ARMOR
  levels:
    '1':
      chance: 19
      cooldown: 6
      effects:
      - POTION:SLOW:0:100 @Attacker
      - MESSAGE:§b§l** FROZEN ** @Attacker
    '2':
      chance: 19
      cooldown: 6
      effects:
      - POTION:SLOW:1:100 @Attacker
      - MESSAGE:§b§l** FROZEN ** @Attacker
    '3':
      chance: 26
      cooldown: 6
      effects:
      - POTION:SLOW:1:100 @Attacker
      - MESSAGE:§b§l** FROZEN ** @Attacker
paralyze:
  display: '%group-color%Paralyze'
  description: |-
    Da lightning efecto y una oportunidad
    para lentitud y balanceado lento.
  applies-to: ꐚ
  type: ATTACK
  group: ELITE
  applies:
  - ALL_SWORD
  levels:
    '1':
      chance: 7
      cooldown: 3
      effects:
      - LIGHTNING @Victim
      - EXTINGUISH @Victim
      - MESSAGE:§b§l** PARALYZE ** @Victim
      - POTION:SLOW:0:60 @Victim
      - POTION:SLOW_DIGGING:0:60 @Victim
    '2':
      chance: 10
      cooldown: 3
      effects:
      - LIGHTNING @Victim
      - EXTINGUISH @Victim
      - MESSAGE:§b§l** PARALYZE ** @Victim
      - POTION:SLOW:0:100 @Victim
      - POTION:SLOW_DIGGING:0:100 @Victim
    '3':
      chance: 13
      cooldown: 3
      effects:
      - LIGHTNING @Victim
      - EXTINGUISH @Victim
      - MESSAGE:§b§l** PARALYZE ** @Victim
      - POTION:SLOW:1:60 @Victim
      - POTION:SLOW_DIGGING:1:60 @Victim
    '4':
      chance: 16
      cooldown: 3
      effects:
      - LIGHTNING @Victim
      - EXTINGUISH @Victim
      - MESSAGE:§b§l** PARALYZE ** @Victim
      - POTION:SLOW:1:100 @Victim
      - POTION:SLOW_DIGGING:1:100 @Victim
poison:
  display: '%group-color%Poison'
  description: Una oportunidad de dar poison efecto.
  applies-to: ꐚ ꐝ
  type: ATTACK;ATTACK_MOB
  group: ELITE
  applies:
  - ALL_SWORD
  - ALL_AXE
  levels:
    '1':
      chance: 6
      cooldown: 2
      effects:
      - POTION:POISON:0:80 @Victim
      - MESSAGE:§b§l** POISON ** @Victim
    '2':
      chance: 12
      cooldown: 2
      effects:
      - POTION:POISON:0:120 @Victim
      - MESSAGE:§b§l** POISON ** @Victim
    '3':
      chance: 19
      cooldown: 2
      effects:
      - POTION:POISON:1:80 @Victim
      - MESSAGE:§b§l** POISON ** @Victim
poisoned:
  display: '%group-color%Poisoned'
  description: Oportunidad de dar poison a tu atacante.
  applies-to: ꐤ ꐞ ꐧ ꐥ
  type: DEFENSE;DEFENSE_MOB;DEFENSE_PROJECTILE
  group: ELITE
  applies:
  - ALL_ARMOR
  levels:
    '1':
      chance: 8
      cooldown: 6
      effects:
      - POTION:POISON:0:60 @Attacker
      - MESSAGE:§b§l** POISONED ** @Attacker
    '2':
      chance: 12
      cooldown: 6
      effects:
      - POTION:POISON:0:120 @Attacker
      - MESSAGE:§b§l** POISONED ** @Attacker
    '3':
      chance: 17
      cooldown: 6
      effects:
      - POTION:POISON:1:60 @Attacker
      - MESSAGE:§b§l** POISONED ** @Attacker
    '4':
      chance: 23
      cooldown: 6
      effects:
      - POTION:POISON:1:120 @Attacker
      - MESSAGE:§b§l** POISONED ** @Attacker
reforged:
  display: '%group-color%Reforged'
  description: |-
    Protege la durabilidad de las armas y las herramientas, los artículos se tomarán
    más para romper.
  applies-to: Weapons and tools
  type: ATTACK_MOB;MINING
  group: ELITE
  applies:
  - ALL_AXE
  - ALL_SWORD
  - ALL_PICKAXE
  - ALL_SPADE
  levels:
    '1':
      chance: 10
      effects:
      - ADD_DURABILITY_ITEM:-1
    '2':
      chance: 20
      effects:
      - ADD_DURABILITY_ITEM:-1
    '3':
      chance: 30
      effects:
      - ADD_DURABILITY_ITEM:-2
    '4':
      chance: 40
      effects:
      - ADD_DURABILITY_ITEM:-2
    '5':
      chance: 50
      effects:
      - ADD_DURABILITY_ITEM:-2
    '6':
      chance: 60
      effects:
      - ADD_DURABILITY_ITEM:-3
    '7':
      chance: 70
      effects:
      - ADD_DURABILITY_ITEM:-3
    '8':
      chance: 80
      effects:
      - ADD_DURABILITY_ITEM:-4
    '9':
      chance: 90
      effects:
      - ADD_DURABILITY_ITEM:-4
    '10':
      effects:
      - ADD_DURABILITY_ITEM:-5
snare:
  display: '%group-color%Snare'
  description: |-
    Oportunidad de ralentizar y fatiga
    Enemigos con proyectiles.
  applies-to: ꐣ
  type: SHOOT;SHOOT_MOB
  group: ELITE
  applies:
  - BOW
  - CROSSBOW
  levels:
    '1':
      chance: 12
      cooldown: 3
      effects:
      - POTION:SLOW:0:80 @Victim
      - POTION:SLOW_DIGGING:0:80 @Victim
    '2':
      chance: 19
      cooldown: 3
      effects:
      - POTION:SLOW:0:120 @Victim
      - POTION:SLOW_DIGGING:0:120 @Victim
    '3':
      chance: 24
      cooldown: 3
      effects:
      - POTION:SLOW:1:80 @Victim
      - POTION:SLOW_DIGGING:1:80 @Victim
    '4':
      chance: 29
      cooldown: 3
      effects:
      - POTION:SLOW:1:120 @Victim
      - POTION:SLOW_DIGGING:1:120 @Victim
springs:
  display: '%group-color%Springs'
  description: Da impulso de salto.
  applies-to: ꐥ
  type: EFFECT_STATIC
  group: ELITE
  applies:
  - ALL_BOOTS
  levels:
    '1':
      effects:
      - POTION:JUMP:0
    '2':
      effects:
      - POTION:JUMP:1
    '3':
      effects:
      - POTION:JUMP:2
stormcaller:
  display: '%group-color%Stormcaller'
  description: Huele lightning en los jugadores atacantes.
  applies-to: ꐤ ꐞ ꐧ ꐥ
  type: DEFENSE;DEFENSE_MOB
  group: ELITE
  applies:
  - ALL_ARMOR
  levels:
    '1':
      chance: 17
      cooldown: 4
      effects:
      - LIGHTNING @Attacker
      - EXTINGUISH @Attacker
    '2':
      chance: 23
      cooldown: 5
      effects:
      - LIGHTNING @Attacker
      - EXTINGUISH @Attacker
    '3':
      chance: 31
      cooldown: 5
      effects:
      - LIGHTNING @Attacker
      - EXTINGUISH @Attacker
    '4':
      chance: 41
      cooldown: 5
      effects:
      - LIGHTNING @Attacker
      - EXTINGUISH @Attacker
demonforged:
  display: '%group-color%Demonforged'
  description: |-
    Aumenta la pérdida de durabilidad en
    La armadura de tu enemigo.
  applies-to: ꐚ
  type: ATTACK
  group: ELITE
  applies:
  - ALL_SWORD
  levels:
    '1':
      cooldown: 6
      chance: 8
      effects:
      - DAMAGE_ARMOR:<random number>1-3</random number> @Victim
    '2':
      cooldown: 6
      chance: 12
      effects:
      - DAMAGE_ARMOR:<random number>1-3</random number> @Victim
    '3':
      cooldown: 6
      chance: 15
      effects:
      - DAMAGE_ARMOR:<random number>1-3</random number> @Victim
    '4':
      cooldown: 6
      chance: 17
      effects:
      - DAMAGE_ARMOR:<random number>1-3</random number> @Victim
trap:
  display: '%group-color%Trap'
  description: Oportunidad de dar efecto de lentitud pulida.
  applies-to: ꐚ
  type: ATTACK;ATTACK_MOB
  group: ELITE
  applies:
  - ALL_SWORD
  levels:
    '1':
      chance: 16
      cooldown: 3
      effects:
      - POTION:SLOW:2:60 @Victim
      - MESSAGE:§b§l** RALENTIZADO ** @Victim
    '2':
      chance: 21
      cooldown: 3
      effects:
      - POTION:SLOW:2:120 @Victim
      - MESSAGE:§b§l** RALENTIZADO ** @Victim
    '3':
      chance: 27
      cooldown: 3
      effects:
      - POTION:SLOW:2:180 @Victim
      - MESSAGE:§b§l** RALENTIZADO ** @Victim
undeadruse:
  display: '%group-color%Undead Ruse'
  description: |-
    Cuando golpeas tienes la oportunidad de engendrar zombie
    Hordas para distraer y desorientar a tus oponentes.
  applies-to: ꐥ
  type: DEFENSE;DEFENSE_MOB
  group: ELITE
  applies:
  - ALL_BOOTS
  levels:
    '1':
      chance: 3
      cooldown: 6
      effects:
      - GUARD:ZOMBIE:@Victim
      - GUARD:ZOMBIE:@Victim
    '2':
      chance: 3
      cooldown: 6
      effects:
      - GUARD:ZOMBIE:@Victim
      - GUARD:ZOMBIE:@Victim
    '3':
      chance: 5
      cooldown: 6
      effects:
      - GUARD:ZOMBIE:@Victim
      - GUARD:ZOMBIE:@Victim
    '4':
      chance: 6
      cooldown: 6
      effects:
      - GUARD:ZOMBIE:@Victim
      - GUARD:ZOMBIE:@Victim
    '5':
      chance: 7
      cooldown: 6
      effects:
      - GUARD:ZOMBIE:@Victim
      - GUARD:ZOMBIE:@Victim
    '6':
      chance: 8
      cooldown: 6
      effects:
      - GUARD:ZOMBIE:@Victim
      - GUARD:ZOMBIE:@Victim
      - GUARD:ZOMBIE:@Victim
    '7':
      chance: 10
      cooldown: 6
      effects:
      - GUARD:ZOMBIE:@Victim
      - GUARD:ZOMBIE:@Victim
      - GUARD:ZOMBIE:@Victim
    '8':
      chance: 14
      cooldown: 6
      effects:
      - GUARD:ZOMBIE:@Victim
      - GUARD:ZOMBIE:@Victim
      - GUARD:ZOMBIE:@Victim
      - GUARD:ZOMBIE:@Victim
    '9':
      chance: 18
      cooldown: 6
      effects:
      - GUARD:ZOMBIE:@Victim
      - GUARD:ZOMBIE:@Victim
      - GUARD:ZOMBIE:@Victim
      - GUARD:ZOMBIE:@Victim
    '10':
      chance: 22
      cooldown: 6
      effects:
      - GUARD:ZOMBIE:@Victim
      - GUARD:ZOMBIE:@Victim
      - GUARD:ZOMBIE:@Victim
      - GUARD:ZOMBIE:@Victim
      - GUARD:ZOMBIE:@Victim
venom:
  display: '%group-color%Venom'
  description: Una oportunidad de tratar poison.
  applies-to: ꐣ
  type: SHOOT;SHOOT_MOB
  group: ELITE
  applies:
  - BOW
  - CROSSBOW
  levels:
    '1':
      chance: 5
      cooldown: 2
      effects:
      - POTION:POISON:0:80 @Victim
    '2':
      chance: 9
      cooldown: 2
      effects:
      - POTION:POISON:0:120 @Victim
    '3':
      chance: 14
      cooldown: 2
      effects:
      - POTION:POISON:1:80 @Victim
voodoo:
  display: '%group-color%Voodoo'
  description: Da la oportunidad de tratar debilidad.
  applies-to: ꐤ ꐞ ꐧ ꐥ
  type: DEFENSE;DEFENSE_MOB
  group: ELITE
  applies:
  - ALL_ARMOR
  levels:
    '1':
      chance: 5
      cooldown: 2
      effects:
      - POTION:WEAKNESS:0:60 @Attacker
    '2':
      chance: 7
      cooldown: 2
      effects:
      - POTION:WEAKNESS:0:100 @Attacker
    '3':
      chance: 9
      cooldown: 2
      effects:
      - POTION:WEAKNESS:0:140 @Attacker
    '4':
      chance: 13
      cooldown: 2
      effects:
      - POTION:WEAKNESS:1:60 @Attacker
    '5':
      chance: 16
      cooldown: 2
      effects:
      - POTION:WEAKNESS:1:100 @Attacker
    '6':
      chance: 21
      cooldown: 2
      effects:
      - POTION:WEAKNESS:1:120 @Attacker
wither:
  display: '%group-color%Wither'
  description: Una oportunidad de dar el efecto wither.
  applies-to: ꐤ ꐞ ꐧ ꐥ
  type: DEFENSE;DEFENSE_MOB
  group: ELITE
  applies:
  - ALL_ARMOR
  levels:
    '1':
      chance: 9
      cooldown: 3
      effects:
      - POTION:WITHER:0:60 @Attacker
    '2':
      chance: 11
      cooldown: 3
      effects:
      - POTION:WITHER:0:100 @Attacker
    '3':
      chance: 14
      cooldown: 3
      effects:
      - POTION:WITHER:0:140 @Attacker
    '4':
      chance: 17
      cooldown: 3
      effects:
      - POTION:WITHER:1:60 @Attacker
    '5':
      chance: 21
      cooldown: 3
      effects:
      - POTION:WITHER:1:100 @Attacker
smokebomb:
  display: '%group-color%Smoke Bomb'
  description: |-
    Cuando estés cerca de la muerte, aparecerás
    una bomba de humo para distraer a tus enemigos.
  applies-to: ꐤ
  type: DEFENSE
  group: ELITE
  applies:
  - ALL_HELMET
  levels:
    '1':
      chance: 9
      cooldown: 2
      conditions:
      - '%victim health% > 4 : %stop%'
      effects:
      - PARTICLE:CLOUD:200:3 @Victim
      - POTION:BLINDNESS:0:60 @Attacker
    '2':
      chance: 15
      cooldown: 2
      conditions:
      - '%victim health% > 4 : %stop%'
      effects:
      - PARTICLE:CLOUD:200:3 @Victim
      - POTION:BLINDNESS:0:60 @Attacker
    '3':
      chance: 23
      cooldown: 2
      conditions:
      - '%victim health% > 4 : %stop%'
      effects:
      - PARTICLE:CLOUD:200:3 @Victim
      - POTION:BLINDNESS:0:100 @Attacker
    '4':
      chance: 28
      cooldown: 2
      conditions:
      - '%victim health% > 5 : %stop%'
      effects:
      - PARTICLE:CLOUD:200:3 @Victim
      - POTION:BLINDNESS:0:100 @Attacker
    '5':
      chance: 30
      cooldown: 2
      conditions:
      - '%victim health% > 5 : %stop%'
      effects:
      - PARTICLE:CLOUD:200:3 @Victim
      - POTION:BLINDNESS:1:60 @Attacker
    '6':
      chance: 34
      cooldown: 2
      conditions:
      - '%victim health% > 5 : %stop%'
      effects:
      - PARTICLE:CLOUD:200:3 @Victim
      - POTION:BLINDNESS:1:100 @Attacker
    '7':
      chance: 36
      cooldown: 2
      conditions:
      - '%victim health% > 6 : %stop%'
      effects:
      - PARTICLE:CLOUD:200:3 @Victim
      - POTION:BLINDNESS:1:140 @Attacker
    '8':
      chance: 38
      cooldown: 2
      conditions:
      - '%victim health% > 6 : %stop%'
      effects:
      - PARTICLE:CLOUD:200:3 @Victim
      - POTION:BLINDNESS:2:120 @Attacker
infernal:
  display: '%group-color%Infernal'
  description: Efecto de fuego explosivo.
  applies-to: ꐣ
  type: SHOOT;SHOOT_MOB
  group: ELITE
  applies:
  - BOW
  - CROSSBOW
  levels:
    '1':
      chance: 15
      cooldown: 2
      effects:
      - PARTICLE:BURN:2:20
      - BURN:2 @Victim
    '2':
      chance: 30
      cooldown: 2
      effects:
      - PARTICLE:BURN:2:40
      - BURN:4 @Victim
    '3':
      chance: 50
      cooldown: 2
      effects:
      - PARTICLE:BURN:3:20
      - BURN:6 @Victim
pummel:
  display: '%group-color%Pummel'
  description: |-
    Oportunidad de frenar el enemigo cercano
    jugadores por un período corto.
  applies-to: ꐝ
  type: ATTACK;ATTACK_MOB
  group: ELITE
  applies:
  - ALL_AXE
  levels:
    '1':
      chance: 17
      cooldown: 4
      effects:
      - POTION:SLOW:0:100 @Victim
      - MESSAGE:§b§l** PUMMEL ** @Victim
    '2':
      chance: 24
      cooldown: 4
      effects:
      - POTION:SLOW:1:100 @Victim
      - MESSAGE:§b§l** PUMMEL ** @Victim
    '3':
      chance: 31
      cooldown: 4
      effects:
      - POTION:SLOW:2:100 @Victim
      - MESSAGE:§b§l** PUMMEL ** @Victim
shockwave:
  display: '%group-color%Shockwave'
  description: |-
    Oportunidad de retrasar a tu atacante
    Cuando tu salud es baja.
  applies-to: ꐧ
  type: DEFENSE
  group: ELITE
  applies:
  - ALL_CHESTPLATE
  levels:
    '1':
      chance: 10
      cooldown: 4
      conditions:
      - '%victim health% > 5 : %stop%'
      effects:
      - PULL_AWAY:0.5 @Attacker
    '2':
      chance: 20
      cooldown: 4
      conditions:
      - '%victim health% > 5 : %stop%'
      effects:
      - PULL_AWAY:1.0 @Attacker
    '3':
      chance: 30
      cooldown: 4
      conditions:
      - '%victim health% > 5 : %stop%'
      effects:
      - PULL_AWAY:1.5 @Attacker
    '4':
      chance: 40
      cooldown: 4
      conditions:
      - '%victim health% > 5 : %stop%'
      effects:
      - PULL_AWAY:2.0 @Attacker
    '5':
      chance: 50
      cooldown: 4
      conditions:
      - '%victim health% > 5 : %stop%'
      effects:
      - PULL_AWAY:2.5 @Attacker
vampire:
  display: '%group-color%Vampire'
  description: |-
    Una oportunidad de curarte hasta
    3hp unos segundos después de usted strike.
  applies-to: ꐚ
  type: ATTACK
  group: ELITE
  applies:
  - ALL_SWORD
  levels:
    '1':
      chance: 7
      cooldown: 4
      effects:
      - WAIT:40
      - ADD_HEALTH:<random number>1-6</random number>
    '2':
      chance: 15
      cooldown: 4
      effects:
      - WAIT:40
      - ADD_HEALTH:<random number>1-6</random number>
    '3':
      chance: 23
      cooldown: 4
      effects:
      - WAIT:40
      - ADD_HEALTH:<random number>1-6</random number>
farcast:
  display: '%group-color%Farcast'
  description: |-
    Oportunidad de retroceder a los atacantes cuerpo a cuerpo
    por un par de bloques cuando te golpean.
    Mayores posibilidades de superar cuando su salud es baja.
  applies-to: ꐣ
  type: SHOOT
  group: ELITE
  applies:
  - BOW
  - CROSSBOW
  levels:
    '1':
      chance: 12
      conditions:
      - '%victim is holding% contains SWORD or %victim is holding% contains AXE :
        %allow%'
      - '%victim health% < 6 : %chance%+3'
      effects:
      - PULL_AWAY:1.0 @Attacker
    '2':
      chance: 20
      conditions:
      - '%victim is holding% contains SWORD or %victim is holding% contains AXE :
        %allow%'
      - '%victim health% < 6 : %chance%+4'
      effects:
      - PULL_AWAY:1.0 @Attacker
    '3':
      chance: 25
      conditions:
      - '%victim is holding% contains SWORD or %victim is holding% contains AXE :
        %allow%'
      - '%victim health% < 6 : %chance%+5'
      effects:
      - PULL_AWAY:2.0 @Attacker
    '4':
      chance: 30
      conditions:
      - '%victim is holding% contains SWORD or %victim is holding% contains AXE :
        %allow%'
      - '%victim health% < 6 : %chance%+6'
      effects:
      - PULL_AWAY:2.0 @Attacker
    '5':
      chance: 35
      conditions:
      - '%victim is holding% contains SWORD or %victim is holding% contains AXE :
        %allow%'
      - '%victim health% < 6 : %chance%+6'
      effects:
      - PULL_AWAY:2.0 @Attacker
greatsword:
  display: '%group-color%Greatsword'
  description: |-
    Multiplica el daño contra los jugadores que son
    empuñando un arco en el momento en que son golpeados.
  applies-to: ꐚ
  type: ATTACK
  group: ELITE
  applies:
  - ALL_SWORD
  levels:
    '1':
      chance: 15
      cooldown: 2
      conditions:
      - '%victim is holding% contains BOW : %allow%'
      effects:
      - INCREASE_DAMAGE:<random number>45-70</random number> @Attacker
      - MESSAGE:§b§l** DAÑO AUMENTADO ** @Attacker
    '2':
      chance: 25
      cooldown: 2
      conditions:
      - '%victim is holding% contains BOW : %allow%'
      effects:
      - INCREASE_DAMAGE:<random number>75-90</random number> @Attacker
      - MESSAGE:§b§l** DAÑO AUMENTADO ** @Attacker
    '3':
      chance: 35
      cooldown: 2
      conditions:
      - '%victim is holding% contains BOW : %allow%'
      effects:
      - INCREASE_DAMAGE:<random number>85-165</random number> @Attacker
      - MESSAGE:§b§l** DAÑO AUMENTADO ** @Attacker
    '4':
      chance: 45
      cooldown: 2
      conditions:
      - '%victim is holding% contains BOW : %allow%'
      effects:
      - INCREASE_DAMAGE:<random number>105-205</random number>
      - MESSAGE:§b§l** DAÑO AUMENTADO ** @Attacker
    '5':
      chance: 55
      cooldown: 2
      conditions:
      - '%victim is holding% contains BOW : %allow%'
      effects:
      - INCREASE_DAMAGE:<random number>105-205</random number>
      - MESSAGE:§b§l** DAÑO AUMENTADO ** @Attacker
hardened:
  display: '%group-color%Hardened'
  description: Chance to recover durability when damaged.
  applies-to: ꐤ ꐞ ꐧ ꐥ
  type: DEFENSE
  group: ELITE
  applies:
  - ALL_ARMOR
  levels:
    '1':
      chance: 25
      cooldown: 7
      effects:
      - ADD_DURABILITY_ARMOR:-1 @Victim
    '2':
      chance: 35
      cooldown: 7
      effects:
      - ADD_DURABILITY_ARMOR:-1 @Victim
    '3':
      chance: 45
      cooldown: 7
      effects:
      - ADD_DURABILITY_ARMOR:-2 @Victim
rocketescape:
  display: '%group-color%Rocket Escape'
  description: Aparece en el aire a bajo HP.
  applies-to: ꐥ
  type: DEFENSE
  group: ELITE
  applies:
  - ALL_BOOTS
  levels:
    '1':
      chance: 20
      cooldown: 8
      conditions:
      - '%victim health% > 6 : %stop%'
      effects:
      - BOOST:30 @Victim
    '2':
      chance: 34
      cooldown: 8
      conditions:
      - '%victim health% > 6 : %stop%'
      effects:
      - BOOST:45 @Victim
    '3':
      chance: 40
      cooldown: 8
      conditions:
      - '%victim health% > 6 : %stop%'
      effects:
      - BOOST:50 @Victim
trickster:
  display: '%group-color%Trickster'
  description: |-
    Cuando golpeas tienes la oportunidad de teletransportar directamente
    Detrás de tu oponente y tómalos por surprise.
  applies-to: ꐤ ꐞ ꐧ ꐥ
  type: DEFENSE
  group: ELITE
  applies:
  - ALL_ARMOR
  levels:
    '1':
      chance: 8
      cooldown: 5
      effects:
      - TELEPORT_BEHIND @Victim
    '2':
      chance: 14
      cooldown: 5
      effects:
      - TELEPORT_BEHIND @Victim
    '3':
      chance: 17
      cooldown: 5
      effects:
      - TELEPORT_BEHIND @Victim
    '4':
      chance: 21
      cooldown: 5
      effects:
      - TELEPORT_BEHIND @Victim
    '5':
      chance: 29
      cooldown: 5
      effects:
      - TELEPORT_BEHIND @Victim
    '6':
      chance: 37
      cooldown: 5
      effects:
      - TELEPORT_BEHIND @Victim
    '7':
      chance: 46
      cooldown: 5
      effects:
      - TELEPORT_BEHIND @Victim
    '8':
      chance: 51
      cooldown: 5
      effects:
      - TELEPORT_BEHIND @Victim
hijack:
  display: '%group-color%Hijack'
  description: |-
    Oportunidad de convertir enemigo invocado
    Guardianes en los tuyos cuando ellos
    son disparados con una flecha.
  applies-to: ꐣ
  type: ATTACK_MOB
  group: ELITE
  applies:
  - BOW
  - CROSSBOW
  levels:
    '1':
      chance: 8
      cooldown: 5
      effects:
      - STEAL_GUARD
    '2':
      chance: 14
      cooldown: 5
      effects:
      - STEAL_GUARD
    '3':
      chance: 17
      cooldown: 5
      effects:
      - STEAL_GUARD
    '4':
      chance: 21
      cooldown: 5
      effects:
      - STEAL_GUARD
timber:
  display: '%group-color%Timber'
  description: Oportunidad de romper un árbol de un golpe
  applies-to: ꐝ
  group: ULTIMATE
  type: MINING
  applies:
  - ALL_AXE
  levels:
    '1':
      chance: 15
      cooldown: 5
      effects:
      - BREAK_TREE @Block
    '2':
      chance: 35
      cooldown: 5
      effects:
      - BREAK_TREE @Block
    '3':
      chance: 55
      cooldown: 6
      effects:
      - BREAK_TREE @Block
pickpocket:
  display: '%group-color%Pickpocket'
  description: Oportunidad de robar dinero en el juego mientras lucha.
  applies-to: ꐚ ꐝ
  type: ATTACK
  group: ULTIMATE
  applies:
  - ALL_SWORD
  - ALL_AXE
  levels:
    '1':
      chance: 3
      cooldown: 80
      effects:
      - STEAL_MONEY:<random number>200-1000</random number> @Victim
      - PLAY_SOUND_OUTLOUD:NOTE_STICKS:10
      - MESSAGE:§9§l** PICKPOCKET ** §7(-§a%random% $§7) @Victim
    '2':
      chance: 5
      cooldown: 80
      effects:
      - STEAL_MONEY:<random number>200-1200</random number> @Victim
      - PLAY_SOUND_OUTLOUD:NOTE_STICKS:10
      - MESSAGE:§9§l** PICKPOCKET ** §7(-§a%random% $§7) @Victim
    '3':
      chance: 6
      cooldown: 80
      effects:
      - STEAL_MONEY:<random number>200-1500</random number> @Victim
      - PLAY_SOUND_OUTLOUD:NOTE_STICKS:10
      - MESSAGE:§9§l** PICKPOCKET ** §7(-§a%random% $§7) @Victim
distance:
  display: '%group-color%Distance'
  description: |-
    Oportunidad de distance tú mismo de tus enemigos
    y ganar regeneración.
  applies-to: ꐚ ꐝ
  type: ATTACK
  group: ULTIMATE
  applies:
  - ALL_SWORD
  - ALL_AXE
  levels:
    '1':
      chance: 16
      cooldown: 6
      effects:
      - PULL_AWAY:3.0 @Victim
      - POTION:REGENERATION:0:20 @Attacker
      - MESSAGE:§a§l** DISTANCE ** §7(§o%attacker name%§7) @Victim
    '2':
      chance: 20
      cooldown: 6
      effects:
      - PULL_AWAY:4.5 @Victim
      - POTION:REGENERATION:0:20 @Attacker
      - MESSAGE:§a§l** DISTANCE ** §7(§o%attacker name%§7) @Victim
    '3':
      chance: 24
      cooldown: 6
      effects:
      - PULL_AWAY:5.0 @Victim
      - POTION:REGENERATION:1:20 @Attacker
      - MESSAGE:§a§l** DISTANCE ** §7(§o%attacker name%§7) @Victim
    '4':
      chance: 28
      cooldown: 6
      effects:
      - PULL_AWAY:6.5 @Victim
      - POTION:REGENERATION:1:40 @Attacker
      - MESSAGE:§a§l** DISTANCE ** §7(§o%attacker name%§7) @Victim
reinforced:
  display: '%group-color% Reinforced'
  description: Tome menos daño al ser golpeado por detrás.
  applies-to: ꐤ ꐞ ꐧ ꐥ
  type: DEFENSE
  group: ULTIMATE
  applies:
  - ALL_ARMOR
  levels:
    '1':
      chance: 9
      cooldown: 3
      conditions:
      - '%damage from behind% = TRUE : %continue%'
      effects:
      - NEGATE_DAMAGE:<random number>1-35</random number>
    '2':
      chance: 12
      cooldown: 3
      conditions:
      - '%damage from behind% = TRUE : %continue%'
      effects:
      - NEGATE_DAMAGE:<random number>1-35</random number>
    '3':
      chance: 15
      cooldown: 3
      conditions:
      - '%damage from behind% = TRUE : %continue%'
      effects:
      - NEGATE_DAMAGE:<random number>1-35</random number>
    '4':
      chance: 18
      cooldown: 3
      conditions:
      - '%damage from behind% = TRUE : %continue%'
      effects:
      - NEGATE_DAMAGE:<random number>1-35</random number>
cleave:
  display: '%group-color%Cleave'
  description: |-
    Daña a los jugadores dentro de un radio
    Eso aumenta con el nivel de encantamiento.
  applies-to: ꐝ
  type: ATTACK
  group: ULTIMATE
  applies:
  - ALL_AXE
  levels:
    '1':
      chance: 4
      cooldown: 8
      effects:
      - DO_HARM:<random number>1-3</random number> @Aoe{r=1,t=damageable}
      - MESSAGE:§e§l** CLEAVE §7(%attacker name%)§e§l ** @Aoe{r=1,t=damageable}
    '2':
      chance: 5
      cooldown: 8
      effects:
      - DO_HARM:<random number>1-3</random number> @Aoe{r=2,t=damageable}
      - MESSAGE:§e§l** CLEAVE §7(%attacker name%)§e§l ** @Aoe{r=2,t=damageable}
    '3':
      chance: 6
      cooldown: 9
      effects:
      - DO_HARM:<random number>1-3</random number> @Aoe{r=3,t=damageable}
      - MESSAGE:§e§l** CLEAVE §7(%attacker name%)§e§l ** @Aoe{r=3,t=damageable}
    '4':
      chance: 7
      cooldown: 9
      effects:
      - DO_HARM:<random number>1-3</random number> @Aoe{r=4,t=damageable}
      - MESSAGE:§e§l** CLEAVE §7(%attacker name%)§e§l ** @Aoe{r=4,t=damageable}
    '5':
      chance: 9
      cooldown: 10
      effects:
      - DO_HARM:<random number>2-3</random number> @Aoe{r=5,t=damageable}
      - MESSAGE:§e§l** CLEAVE §7(%attacker name%)§e§l ** @Aoe{r=5,t=damageable}
    '6':
      chance: 12
      cooldown: 12
      effects:
      - DO_HARM:<random number>2-3</random number> @Aoe{r=6,t=damageable}
      - MESSAGE:§e§l** CLEAVE §7(%attacker name%)§e§l ** @Aoe{r=6,t=damageable}
    '7':
      chance: 15
      cooldown: 14
      effects:
      - DO_HARM:<random number>2-3</random number> @Aoe{r=7,t=damageable}
      - MESSAGE:§e§l** CLEAVE §7(%attacker name%)§e§l ** @Aoe{r=7,t=damageable}
angelic:
  display: '%group-color%Angelic'
  description: Cura la salud cuando se daña.
  applies-to: ꐤ ꐞ ꐧ ꐥ
  type: DEFENSE;DEFENSE_MOB
  group: ULTIMATE
  applies:
  - ALL_ARMOR
  levels:
    '1':
      chance: 9
      cooldown: 7
      effects:
      - ADD_HEALTH:<random number>1-3</random number> @Victim
      - MESSAGE:§e§l** ANGELIC ** §7(§c+ %random%HP§7) @Victim
    '2':
      chance: 14
      cooldown: 9
      effects:
      - ADD_HEALTH:<random number>1-3</random number> @Victim
      - MESSAGE:§e§l** ANGELIC ** §7(§c+ %random%HP§7) @Victim
    '3':
      chance: 17
      cooldown: 11
      effects:
      - ADD_HEALTH:<random number>1-3</random number> @Victim
      - MESSAGE:§e§l** ANGELIC ** §7(§c+ %random%HP§7) @Victim
    '4':
      chance: 26
      cooldown: 13
      effects:
      - ADD_HEALTH:<random number>1-4</random number> @Victim
      - MESSAGE:§e§l** ANGELIC ** §7(§c+ %random%HP§7) @Victim
    '5':
      chance: 34
      cooldown: 15
      effects:
      - ADD_HEALTH:<random number>1-4</random number> @Victim
      - MESSAGE:§e§l** ANGELIC ** §7(§c+ %random%HP§7) @Victim
arrowlifesteal:
  display: '%group-color%Arrow Lifesteal'
  description: Chance to steal health from opponent.
  applies-to: ꐣ
  type: SHOOT
  group: ULTIMATE
  applies:
  - BOW
  - CROSSBOW
  levels:
    '1':
      chance: 7
      cooldown: 2
      effects:
      - STEAL_HEALTH:<random number>1-4</random number>
    '2':
      chance: 12
      cooldown: 2
      effects:
      - STEAL_HEALTH:<random number>1-4</random number>
    '3':
      chance: 17
      cooldown: 2
      effects:
      - STEAL_HEALTH:<random number>1-4</random number>
    '4':
      chance: 22
      cooldown: 2
      effects:
      - STEAL_HEALTH:<random number>1-4</random number>
    '5':
      chance: 27
      cooldown: 2
      effects:
      - STEAL_HEALTH:<random number>1-4</random number>
arrowdeflect:
  display: '%group-color%Arrow Deflect'
  description: Oportunidad de evitar que la flecha enemiga cause daño.
  applies-to: ꐤ ꐞ ꐧ ꐥ
  type: DEFENSE_PROJECTILE
  group: ULTIMATE
  applies:
  - ALL_ARMOR
  levels:
    '1':
      chance: 15
      cooldown: 6
      effects:
      - CANCEL_EVENT
      - MESSAGE:§e§l* ARROW DEFLECT * @Victim
    '2':
      chance: 25
      cooldown: 6
      effects:
      - CANCEL_EVENT
      - MESSAGE:§e§l* ARROW DEFLECT * @Victim
    '3':
      chance: 35
      cooldown: 6
      effects:
      - CANCEL_EVENT
      - MESSAGE:§e§l* ARROW DEFLECT * @Victim
    '4':
      chance: 45
      cooldown: 6
      effects:
      - MESSAGE:§e§l* ARROW DEFLECT * @Victim
      - CANCEL_EVENT
arrowbreak:
  display: '%group-color%Arrow Break'
  description: |-
    Posibilidad de que las flechas reboten
    y no te dañes cuando
    Estás empuñando un hacha con esto
    encanto en él.
  applies-to: ꐝ
  type: DEFENSE_PROJECTILE
  group: ULTIMATE
  applies:
  - ALL_AXE
  levels:
    '1':
      chance: 15
      cooldown: 8
      effects:
      - CANCEL_EVENT
      - MESSAGE:§e§l** ARROW BREAK ** @Victim
      - PLAY_SOUND:ITEM_BREAK:2 @Victim
    '2':
      chance: 25
      cooldown: 8
      effects:
      - CANCEL_EVENT
      - MESSAGE:§e§l** ARROW BREAK ** @Victim
      - PLAY_SOUND:ITEM_BREAK:2 @Victim
    '3':
      chance: 35
      cooldown: 8
      effects:
      - CANCEL_EVENT
      - MESSAGE:§e§l** ARROW BREAK ** @Victim
      - PLAY_SOUND:ITEM_BREAK:2 @Victim
    '4':
      chance: 45
      cooldown: 9
      effects:
      - CANCEL_EVENT
      - MESSAGE:§e§l** ARROW BREAK ** @Victim
      - PLAY_SOUND:ITEM_BREAK:2 @Victim
    '5':
      chance: 55
      cooldown: 9
      effects:
      - CANCEL_EVENT
      - MESSAGE:§e§l** ARROW BREAK ** @Victim
      - PLAY_SOUND:ITEM_BREAK:2 @Victim
    '6':
      chance: 65
      cooldown: 10
      effects:
      - CANCEL_EVENT
      - MESSAGE:§e§l** ARROW BREAK ** @Victim
      - PLAY_SOUND:ITEM_BREAK:2 @Victim
assassin:
  display: '%group-color%Assassin'
  description: |-
    Cuanto más cerca estés con tu enemigo,
    Cuanto más daño cause (hasta 1.25x).
    Sin embargo, si tienes más de 2
    bloquea, usted tratará menos
    daño de lo normal.
  applies-to: ꐚ
  type: ATTACK
  group: ULTIMATE
  applies:
  - ALL_SWORD
  levels:
    '1':
      chance: 7
      cooldown: 7
      effects:
      - 'MESSAGE:&c(Removed) DISTANCE_DAMAGE:3:1 @Attacker'
    '2':
      chance: 12
      cooldown: 8
      effects:
      - MESSAGE:&c(Removed) DISTANCE_DAMAGE:3:1 @Attacker
    '3':
      chance: 19
      cooldown: 8
      effects:
      - MESSAGE:&c(Removed) DISTANCE_DAMAGE:3:1 @Attacker
    '4':
      chance: 24
      cooldown: 8
      effects:
      - MESSAGE:&c(Removed) DISTANCE_DAMAGE:3:1 @Attacker
    '5':
      chance: 29
      cooldown: 8
      effects:
      - MESSAGE:&c(Removed) DISTANCE_DAMAGE:3:1 @Attacker
blessed:
  display: '%group-color%Blessed'
  description: Una oportunidad de eliminar debuffs.
  applies-to: ꐝ
  type: ATTACK
  group: ULTIMATE
  applies:
  - ALL_AXE
  levels:
    '1':
      chance: 12
      cooldown: 8
      effects:
      - CURE_PERMANENT:SLOW @Attacker
      - CURE_PERMANENT:CONFUSION @Attacker
      - CURE_PERMANENT:BLINDNESS @Attacker
      - CURE_PERMANENT:POISON @Attacker
      - CURE_PERMANENT:WITHER @Attacker
      - CURE_PERMANENT:HUNGER @Attacker
      - CURE_PERMANENT:WEAKNESS @Attacker
      - CURE_PERMANENT:SLOW_DIGGING @Attacker
      - MESSAGE:§e§l** BLESSED ** @Attacker
    '2':
      chance: 16
      cooldown: 8
      effects:
      - CURE_PERMANENT:SLOW @Attacker
      - CURE_PERMANENT:CONFUSION @Attacker
      - CURE_PERMANENT:BLINDNESS @Attacker
      - CURE_PERMANENT:POISON @Attacker
      - CURE_PERMANENT:WITHER @Attacker
      - CURE_PERMANENT:HUNGER @Attacker
      - CURE_PERMANENT:WEAKNESS @Attacker
      - CURE_PERMANENT:SLOW_DIGGING @Attacker
      - MESSAGE:§e§l** BLESSED ** @Attacker
    '3':
      chance: 22
      cooldown: 8
      effects:
      - CURE_PERMANENT:SLOW @Attacker
      - CURE_PERMANENT:CONFUSION @Attacker
      - CURE_PERMANENT:BLINDNESS @Attacker
      - CURE_PERMANENT:POISON @Attacker
      - CURE_PERMANENT:WITHER @Attacker
      - CURE_PERMANENT:HUNGER @Attacker
      - CURE_PERMANENT:WEAKNESS @Attacker
      - CURE_PERMANENT:SLOW_DIGGING @Attacker
      - MESSAGE:§e§l** BLESSED ** @Attacker
    '4':
      chance: 36
      cooldown: 8
      effects:
      - CURE_PERMANENT:SLOW @Attacker
      - CURE_PERMANENT:CONFUSION @Attacker
      - CURE_PERMANENT:BLINDNESS @Attacker
      - CURE_PERMANENT:POISON @Attacker
      - CURE_PERMANENT:WITHER @Attacker
      - CURE_PERMANENT:HUNGER @Attacker
      - CURE_PERMANENT:WEAKNESS @Attacker
      - CURE_PERMANENT:SLOW_DIGGING @Attacker
      - MESSAGE:§e§l** BLESSED ** @Attacker
corrupt:
  display: '%group-color%Corrupt'
  description: Causa daños con el tiempo.
  applies-to: ꐝ
  type: ATTACK
  group: ULTIMATE
  applies:
  - ALL_AXE
  levels:
    '1':
      chance: 12
      cooldown: 4
      effects:
      - DO_HARM:<random number>2-3</random number> @Victim
      - WAIT:20
      - DO_HARM:<random number>2-3</random number> @Victim
      - WAIT:40
      - DO_HARM:<random number>2-3</random number> @Victim
    '2':
      chance: 19
      cooldown: 4
      effects:
      - DO_HARM:<random number>2-3</random number> @Victim
      - WAIT:20
      - DO_HARM:<random number>2-3</random number> @Victim
      - WAIT:40
      - DO_HARM:<random number>2-3</random number> @Victim
    '3':
      chance: 24
      cooldown: 4
      effects:
      - DO_HARM:<random number>2-3</random number> @Victim
      - WAIT:20
      - DO_HARM:<random number>2-3</random number> @Victim
      - WAIT:40
      - DO_HARM:<random number>2-3</random number> @Victim
    '4':
      chance: 31
      cooldown: 4
      effects:
      - DO_HARM:<random number>2-3</random number> @Victim
      - WAIT:20
      - DO_HARM:<random number>2-3</random number> @Victim
      - WAIT:40
      - DO_HARM:<random number>2-3</random number> @Victim
ragdoll:
  display: '%group-color%Ragdoll'
  description: |-
    Siempre que recibas daños
    Te empujan muy hacia atrás.
  applies-to: ꐤ ꐞ ꐧ ꐥ
  type: DEFENSE;DEFENSE_MOB
  group: ULTIMATE
  applies:
  - ALL_ARMOR
  levels:
    '1':
      chance: 10
      cooldown: 4
      effects:
      - PULL_AWAY:0.2 @Victim
    '2':
      chance: 20
      cooldown: 4
      effects:
      - PULL_AWAY:0.3 @Victim
    '3':
      chance: 30
      cooldown: 4
      effects:
      - PULL_AWAY:0.4 @Victim
    '4':
      chance: 50
      cooldown: 4
      effects:
      - PULL_AWAY:0.5 @Victim
block:
  display: '%group-color%Block'
  description: Una oportunidad de negar un ataque y hacer un daño hasta 4 daños.
  applies-to: ꐚ
  type: DEFENSE;DEFENSE_MOB
  group: ULTIMATE
  applies:
  - ALL_SWORD
  levels:
    '1':
      chance: 16
      cooldown: 4
      effects:
      - NEGATE_DAMAGE:50 @Victim
      - DO_HARM:<random number>1-4</random number> @Attacker
    '2':
      chance: 22
      cooldown: 4
      effects:
      - NEGATE_DAMAGE:50 @Victim
      - DO_HARM:<random number>1-4</random number> @Attacker
    '3':
      chance: 30
      cooldown: 4
      effects:
      - NEGATE_DAMAGE:50 @Victim
      - DO_HARM:<random number>1-4</random number> @Attacker
detonate:
  display: '%group-color%Detonate'
  description: Oportunidad de romper en un área de 3x3.
  applies-to: Pickaxes and shovels
  type: MINING
  group: ULTIMATE
  applies:
  - ALL_PICKAXE
  - ALL_SPADE
  levels:
    '1':
      chance: 13
      effects:
      - BREAK_BLOCK @Trench{r=3}
    '2':
      chance: 26
      effects:
      - BREAK_BLOCK @Trench{r=3}
    '3':
      chance: 36
      effects:
      - BREAK_BLOCK @Trench{r=3}
    '4':
      chance: 49
      effects:
      - BREAK_BLOCK @Trench{r=3}
    '5':
      chance: 59
      effects:
      - BREAK_BLOCK @Trench{r=3}
    '6':
      chance: 72
      effects:
      - BREAK_BLOCK @Trench{r=3}
    '7':
      chance: 85
      effects:
      - BREAK_BLOCK @Trench{r=3}
    '8':
      chance: 90
      effects:
      - BREAK_BLOCK @Trench{r=3}
    '9':
      chance: 100
      effects:
      - BREAK_BLOCK @Trench{r=3}
dodge:
  display: '%group-color%Dodge'
  description: |-
    Oportunidad de dodge Enemigo físico
    ataques, mayor oportunidad si
    furtivo.
  applies-to: ꐤ ꐞ ꐧ ꐥ
  type: DEFENSE
  group: ULTIMATE
  applies:
  - ALL_ARMOR
  levels:
    '1':
      chance: 7
      cooldown: 8
      conditions:
      - '%victim is sneaking% = true : %chance%+7'
      effects:
      - CANCEL_EVENT
      - MESSAGE:§e§l*DODGE* @Victim
      - PLAY_SOUND:BAT_TAKEOFF:0.7 @Victim
    '2':
      chance: 12
      cooldown: 8
      conditions:
      - '%victim is sneaking% = true : %chance%+7'
      effects:
      - CANCEL_EVENT
      - MESSAGE:§e§l*DODGE* @Victim
      - PLAY_SOUND:BAT_TAKEOFF:0.7 @Victim
    '3':
      chance: 16
      cooldown: 8
      conditions:
      - '%victim is sneaking% = true : %chance%+7'
      effects:
      - CANCEL_EVENT
      - MESSAGE:§e§l*DODGE* @Victim
      - PLAY_SOUND:BAT_TAKEOFF:0.7 @Victim
    '4':
      chance: 22
      cooldown: 8
      conditions:
      - '%victim is sneaking% = true : %chance%+7'
      effects:
      - CANCEL_EVENT
      - MESSAGE:§e§l*DODGE* @Victim
      - PLAY_SOUND:BAT_TAKEOFF:0.7 @Victim
    '5':
      chance: 27
      cooldown: 8
      conditions:
      - '%victim is sneaking% = true : %chance%+7'
      effects:
      - CANCEL_EVENT
      - MESSAGE:§e§l*DODGE* @Victim
      - PLAY_SOUND:BAT_TAKEOFF:0.7 @Victim
enrage:
  display: '%group-color%Enrage'
  description: Inflige más daño en HP bajo.
  applies-to: ꐚ
  type: ATTACK
  group: ULTIMATE
  applies:
  - ALL_SWORD
  levels:
    '1':
      chance: 21
      cooldown: 5
      conditions:
      - '%attacker health% > 6 : %stop%'
      effects:
      - DO_HARM:<random number>1-4</random number> @Victim
    '2':
      chance: 27
      cooldown: 5
      conditions:
      - '%attacker health% > 6 : %stop%'
      effects:
      - DO_HARM:<random number>1-4</random number> @Victim
    '3':
      chance: 33
      cooldown: 5
      conditions:
      - '%attacker health% > 6 : %stop%'
      effects:
      - DO_HARM:<random number>1-4</random number> @Victim
guardians:
  display: '%group-color%Guardians'
  description: |-
    Una oportunidad de generar golems de hierro para
    ayudarte y cuidarte.
  applies-to: ꐤ ꐞ ꐧ ꐥ
  type: DEFENSE
  group: ULTIMATE
  applies:
  - ALL_ARMOR
  levels:
    '1':
      chance: 6
      cooldown: 8
      effects:
      - GUARD:IRON_GOLEM:@Victim
    '2':
      chance: 9
      cooldown: 8
      effects:
      - GUARD:IRON_GOLEM:@Victim
    '3':
      chance: 13
      cooldown: 8
      effects:
      - GUARD:IRON_GOLEM:@Victim
    '4':
      chance: 14
      cooldown: 8
      effects:
      - GUARD:IRON_GOLEM:@Victim
    '5':
      chance: 16
      cooldown: 9
      effects:
      - GUARD:IRON_GOLEM:@Victim
    '6':
      chance: 17
      cooldown: 10
      effects:
      - GUARD:IRON_GOLEM:@Victim
      - GUARD:IRON_GOLEM:@Victim
    '7':
      chance: 18
      cooldown: 12
      effects:
      - GUARD:IRON_GOLEM:@Victim
      - GUARD:IRON_GOLEM:@Victim
    '8':
      chance: 20
      cooldown: 12
      effects:
      - GUARD:IRON_GOLEM:@Victim
      - GUARD:IRON_GOLEM:@Victim
      - GUARD:IRON_GOLEM:@Victim
    '9':
      chance: 22
      cooldown: 15
      effects:
      - GUARD:IRON_GOLEM:@Victim
      - GUARD:IRON_GOLEM:@Victim
      - GUARD:IRON_GOLEM:@Victim
    '10':
      chance: 24
      cooldown: 15
      effects:
      - GUARD:IRON_GOLEM:@Victim
      - GUARD:IRON_GOLEM:@Victim
      - GUARD:IRON_GOLEM:@Victim
      - GUARD:IRON_GOLEM:@Victim
iceaspect:
  display: '%group-color%Ice Aspect'
  description: |-
    Una posibilidad de causar la lentitud
    efecto en tu enemigo.
  applies-to: ꐚ
  type: ATTACK;ATTACK_MOB
  group: ULTIMATE
  applies:
  - ALL_SWORD
  levels:
    '1':
      chance: 15
      cooldown: 2
      effects:
      - POTION:SLOW:1:100 @Victim
    '2':
      chance: 23
      cooldown: 2
      effects:
      - POTION:SLOW:1:100 @Victim
    '3':
      chance: 31
      cooldown: 2
      effects:
      - POTION:SLOW:1:100 @Victim
implants:
  display: '%group-color%Implants'
  description: |-
    La oportunidad de curar pasivamente +1 salud
    y restaura +1 hambre cada pocos segundos
  applies-to: ꐤ
  type: REPEATING
  time: 5
  group: ULTIMATE
  applies:
  - ALL_HELMET
  levels:
    '1':
      chance: 30
      effects:
      - ADD_HEALTH:1
      - ADD_FOOD:1
    '2':
      chance: 50
      effects:
      - ADD_HEALTH:1
      - ADD_FOOD:1
    '3':
      chance: 70
      effects:
      - ADD_HEALTH:1
      - ADD_FOOD:1
obsidianshield:
  display: '%group-color%Obsidianshield'
  description: Da resistencia permanente al fuego.
  applies-to: ꐤ ꐞ ꐧ ꐥ
  type: EFFECT_STATIC
  group: ULTIMATE
  applies:
  - ALL_ARMOR
  levels:
    '1':
      effects:
      - POTION:FIRE_RESISTANCE:0
demonic:
  display: '%group-color%Demonic'
  description: Una oportunidad de eliminar la resistencia al fuego de tu enemigo.
  applies-to: ꐤ ꐞ ꐧ ꐥ
  type: ATTACK
  group: ULTIMATE
  applies:
  - ALL_ARMOR
  levels:
    '1':
      chance: 9
      cooldown: 2
      effects:
      - CURE:FIRE_RESISTANCE @Victim
      - CURE_PERMANENT:FIRE_RESISTANCE @Victim
    '2':
      chance: 14
      cooldown: 2
      effects:
      - CURE:FIRE_RESISTANCE @Victim
      - CURE_PERMANENT:FIRE_RESISTANCE @Victim
    '3':
      chance: 20
      cooldown: 2
      effects:
      - CURE:FIRE_RESISTANCE @Victim
      - CURE_PERMANENT:FIRE_RESISTANCE @Victim
piercing:
  display: '%group-color%Piercing'
  description: Inflige más daño.
  applies-to: ꐣ
  type: SHOOT
  group: ULTIMATE
  applies:
  - BOW
  - CROSSBOW
  levels:
    '1':
      chance: 13
      cooldown: 3
      effects:
      - INCREASE_DAMAGE:<random number>50-150</random number> @Victim
    '2':
      chance: 19
      cooldown: 3
      effects:
      - INCREASE_DAMAGE:<random number>50-150</random number> @Victim
    '3':
      chance: 25
      cooldown: 3
      effects:
      - INCREASE_DAMAGE:<random number>50-150</random number> @Victim
    '4':
      chance: 32
      cooldown: 3
      effects:
      - INCREASE_DAMAGE:<random number>50-150</random number> @Victim
    '5':
      chance: 37
      cooldown: 3
      effects:
      - INCREASE_DAMAGE:<random number>50-150</random number> @Victim
marksman:
  display: '%group-color%Marksman'
  description: Aumenta el daño tratado con arcos.
  applies-to: ꐤ ꐞ ꐧ ꐥ
  type: ATTACK
  group: ULTIMATE
  applies:
  - ALL_ARMOR
  levels:
    '1':
      chance: 13
      cooldown: 3
      conditions:
      - '%attacker is holding% = BOW : %allow%'
      effects:
      - INCREASE_DAMAGE:<random number>50-150</random number> @Victim
    '2':
      chance: 19
      cooldown: 3
      conditions:
      - '%attacker is holding% = BOW : %allow%'
      effects:
      - INCREASE_DAMAGE:<random number>50-150</random number> @Victim
    '3':
      chance: 25
      cooldown: 3
      conditions:
      - '%attacker is holding% = BOW : %allow%'
      effects:
      - INCREASE_DAMAGE:<random number>50-150</random number> @Victim
    '4':
      chance: 32
      cooldown: 3
      conditions:
      - '%attacker is holding% = BOW : %allow%'
      effects:
      - INCREASE_DAMAGE:<random number>50-150</random number> @Victim
disappear:
  display: '%group-color%Disappear'
  description: |-
    Oportunidad de volverse invisible cuando
    bajo en salud.
  applies-to: ꐤ ꐞ ꐧ ꐥ
  type: DEFENSE
  group: ULTIMATE
  applies:
  - ALL_ARMOR
  levels:
    '1':
      chance: 20
      cooldown: 20
      conditions:
      - '%victim health% > 5 : %stop%'
      effects:
      - POTION:INVISIBILITY:2:60 @Victim
    '2':
      chance: 23
      cooldown: 20
      conditions:
      - '%victim health% > 6 : %stop%'
      effects:
      - POTION:INVISIBILITY:2:80 @Victim
    '3':
      chance: 26
      cooldown: 20
      conditions:
      - '%victim health% > 6 : %stop%'
      effects:
      - POTION:INVISIBILITY:2:100 @Victim
    '4':
      chance: 30
      cooldown: 20
      conditions:
      - '%victim health% > 6 : %stop%'
      effects:
      - POTION:INVISIBILITY:2:120 @Victim
disintegrate:
  display: '%group-color%Disintegrate'
  description: |-
    Oportunidad de causar daño de durabilidad adicional a
    Toda la armadura enemiga con cada ataque.
  applies-to: ꐚ
  type: ATTACK
  group: ULTIMATE
  applies:
  - ALL_SWORD
  levels:
    '1':
      chance: 12
      cooldown: 2
      effects:
      - DAMAGE_ARMOR:2 @Victim
    '2':
      chance: 25
      cooldown: 2
      effects:
      - DAMAGE_ARMOR:2 @Victim
    '3':
      chance: 39
      cooldown: 2
      effects:
      - DAMAGE_ARMOR:2 @Victim
    '4':
      chance: 46
      cooldown: 2
      effects:
      - DAMAGE_ARMOR:2 @Victim
dominate:
  display: '%group-color%Dominate'
  description: |-
    Oportunidad de debilitar a los jugadores enemigos cuando están atacados,
    haciendo que causen menos daño.
  applies-to: ꐚ
  type: DEFENSE;DEFENSE_MOB
  group: ULTIMATE
  applies:
  - ALL_SWORD
  levels:
    '1':
      chance: 15
      cooldown: 3
      effects:
      - POTION:WEAKNESS:0:80 @Attacker
    '2':
      chance: 22
      cooldown: 3
      effects:
      - POTION:WEAKNESS:0:80 @Attacker
    '3':
      chance: 28
      cooldown: 3
      effects:
      - POTION:WEAKNESS:0:80 @Attacker
    '4':
      chance: 35
      cooldown: 3
      effects:
      - POTION:WEAKNESS:0:80 @Attacker
arsonist:
  display: '%group-color%Arsonist'
  description: |-
    Oportunidad de causar más daño
    Mientras está en llamas
  applies-to: ꐚ
  type: ATTACK
  group: ULTIMATE
  applies:
  - ALL_SWORD
  levels:
    '1':
      chance: 8
      cooldown: 5
      conditions:
      - '%attacker is on fire% = true : %allow%'
      effects:
      - DO_HARM:<random number>1-2</random number> @Victim
    '2':
      chance: 12
      cooldown: 5
      conditions:
      - '%attacker is on fire% = true : %allow%'
      effects:
      - DO_HARM:<random number>2-3</random number> @Victim
    '3':
      chance: 16
      cooldown: 8
      conditions:
      - '%attacker is on fire% = true : %allow%'
      effects:
      - DO_HARM:3 @Victim
enderwalker:
  display: '%group-color%Ender Walker'
  description: |-
    Oportunidad de curarse y envenenar cuando se atacan
    nand sanar en niveles altos.
  applies-to: ꐥ
  type: DEFENSE
  group: ULTIMATE
  applies:
  - ALL_BOOTS
  levels:
    '1':
      chance: 9
      cooldown: 8
      effects:
      - CURE:WITHER @Victim
      - CURE:POISON @Victim
    '2':
      chance: 14
      cooldown: 8
      effects:
      - CURE:WITHER @Victim
      - CURE:POISON @Victim
    '3':
      chance: 21
      cooldown: 10
      effects:
      - CURE:WITHER @Victim
      - CURE:POISON @Victim
    '4':
      chance: 28
      cooldown: 13
      effects:
      - CURE:WITHER @Victim
      - CURE:POISON @Victim
      - ADD_HEALTH:<random number>1-4</random number> @Victim
    '5':
      chance: 35
      cooldown: 14
      effects:
      - CURE:WITHER @Victim
      - CURE:POISON @Victim
      - ADD_HEALTH:<random number>1-4</random number> @Victim
eagleeye:
  display: '%group-color%Eagle Eye'
  description: |-
    Oportunidad de otorgar 1-4 daños de durabilidad a
    Todas las armaduras del jugador enemigo.
  applies-to: ꐣ
  type: SHOOT
  group: ULTIMATE
  applies:
  - BOW
  - CROSSBOW
  levels:
    '1':
      chance: 15
      cooldown: 4
      effects:
      - DAMAGE_ARMOR:<random number>1-4</random number> @Victim
    '2':
      chance: 26
      cooldown: 4
      effects:
      - DAMAGE_ARMOR:<random number>1-4</random number> @Victim
    '3':
      chance: 37
      cooldown: 4
      effects:
      - DAMAGE_ARMOR:<random number>1-4</random number> @Victim
    '4':
      chance: 44
      cooldown: 4
      effects:
      - DAMAGE_ARMOR:<random number>1-4</random number> @Victim
    '5':
      chance: 56
      cooldown: 4
      effects:
      - DAMAGE_ARMOR:<random number>1-4</random number> @Victim
annihilate:
  display: '%group-color%Annihilate'
  description: ¡Demoler la armadura de tu oponente más rápido!
  applies-to: ꐝ
  type: ATTACK
  group: ULTIMATE
  applies:
  - ALL_AXE
  levels:
    '1':
      chance: 10
      cooldown: 10
      effects:
      - DAMAGE_ARMOR:1 @Victim
    '2':
      chance: 20
      cooldown: 12
      effects:
      - DAMAGE_ARMOR:1 @Victim
    '3':
      chance: 30
      cooldown: 15
      effects:
      - DAMAGE_ARMOR:2 @Victim
    '4':
      chance: 40
      cooldown: 18
      effects:
      - DAMAGE_ARMOR:2 @Victim
    '5':
      chance: 50
      cooldown: 20
      effects:
      - DAMAGE_ARMOR:3 @Victim
    '6':
      chance: 55
      cooldown: 28
      effects:
      - DAMAGE_ARMOR:4 @Victim
heavy:
  display: '%group-color%Heavy'
  description: |-
    Disminuye el daño de los arcos enemigos
    por 2% por nivel.
  applies-to: ꐤ ꐞ ꐧ ꐥ
  type: DEFENSE
  group: ULTIMATE
  applies:
  - ALL_ARMOR
  levels:
    '1':
      chance: 4
      cooldown: 4
      conditions:
      - '%attacker is holding% = BOW : %continue%'
      effects:
      - DECREASE_DAMAGE:2 @Victim
    '2':
      chance: 9
      cooldown: 4
      conditions:
      - '%attacker is holding% = BOW : %continue%'
      effects:
      - DECREASE_DAMAGE:4 @Victim
    '3':
      chance: 12
      cooldown: 4
      conditions:
      - '%attacker is holding% = BOW : %continue%'
      effects:
      - DECREASE_DAMAGE:6 @Victim
    '4':
      chance: 16
      cooldown: 4
      conditions:
      - '%attacker is holding% = BOW : %continue%'
      effects:
      - DECREASE_DAMAGE:8 @Victim
    '5':
      chance: 21
      cooldown: 4
      conditions:
      - '%attacker is holding% = BOW : %continue%'
      effects:
      - DECREASE_DAMAGE:10 @Victim
hellfire:
  display: '%group-color%Hellfire'
  description: |-
    Todas las flechas disparadas por ti giras
    en explosive bolas de fuego cuando
    en contacto con el enemigo.
  applies-to: ꐣ
  type: SHOOT
  group: ULTIMATE
  applies:
  - BOW
  - CROSSBOW
  levels:
    '1':
      chance: 10
      cooldown: 3
      effects:
      - FIREBALL @Victim
    '2':
      chance: 25
      cooldown: 3
      effects:
      - FIREBALL @Victim
    '3':
      chance: 35
      cooldown: 3
      effects:
      - FIREBALL @Victim
    '4':
      chance: 50
      cooldown: 3
      effects:
      - FIREBALL @Victim
    '5':
      chance: 70
      cooldown: 3
      effects:
      - FIREBALL @Victim
longbow:
  display: '%group-color%Longbow'
  description: |-
    Aumenta enormemente el daño tratado
    a los jugadores enemigos que tienen
    un arco en sus manos.
  applies-to: ꐣ
  type: SHOOT
  group: ULTIMATE
  applies:
  - BOW
  - CROSSBOW
  levels:
    '1':
      chance: 12
      cooldown: 4
      conditions:
      - '%victim is holding% = BOW : %allow%'
      effects:
      - INCREASE_DAMAGE:<random number>25-50</random number> @Attacker
    '2':
      chance: 17
      cooldown: 4
      conditions:
      - '%victim is holding% = BOW : %allow%'
      effects:
      - INCREASE_DAMAGE:<random number>25-50</random number> @Attacker
    '3':
      chance: 25
      cooldown: 4
      conditions:
      - '%victim is holding% = BOW : %allow%'
      effects:
      - INCREASE_DAMAGE:<random number>50-100</random number> @Attacker
    '4':
      chance: 33
      cooldown: 4
      conditions:
      - '%victim is holding% = BOW : %allow%'
      effects:
      - INCREASE_DAMAGE:<random number>50-100</random number> @Attacker
tank:
  display: '%group-color%Tank'
  description: |-
    Oportunidad de disminuir el daño del enemigo
    ejes por 2% por nivel.
  applies-to: ꐤ ꐞ ꐧ ꐥ
  type: DEFENSE
  group: ULTIMATE
  applies:
  - ALL_ARMOR
  levels:
    '1':
      chance: 5
      cooldown: 3
      conditions:
      - '%attacker is holding% contains AXE : %allow%'
      effects:
      - DECREASE_DAMAGE:2 @Victim
    '2':
      chance: 8
      cooldown: 3
      conditions:
      - '%attacker is holding% contains AXE : %allow%'
      effects:
      - DECREASE_DAMAGE:4 @Victim
    '3':
      chance: 12
      cooldown: 3
      conditions:
      - '%attacker is holding% contains AXE : %allow%'
      effects:
      - DECREASE_DAMAGE:6 @Victim
    '4':
      chance: 16
      cooldown: 3
      conditions:
      - '%attacker is holding% contains AXE : %allow%'
      effects:
      - DECREASE_DAMAGE:8 @Victim
unfocus:
  display: '%group-color%Unfocus'
  description: |-
    Oportunidad de soltar el jugador objetivo,
    Reduciendo su daño de la proa yendo
    en un 50% por hasta 10 segundos.
  applies-to: ꐣ
  type: SHOOT
  group: ULTIMATE
  applies:
  - BOW
  - CROSSBOW
  levels:
    '1':
      chance: 7
      cooldown: 4
      effects:
      - POTION:CONFUSION:0:40 @Victim
      - HALF_DAMAGE
      - MESSAGE:§e§l** YOU'VE BEEN UNFOCUSED ** @Victim
      - WAIT:45
      - MESSAGE:§a§l** YOU'VE REGAINED FOCUS ** @Victim
    '2':
      chance: 13
      cooldown: 4
      effects:
      - POTION:CONFUSION:0:80 @Victim
      - HALF_DAMAGE
      - MESSAGE:§e§l** YOU'VE BEEN UNFOCUSED ** @Victim
      - WAIT:85
      - MESSAGE:§a§l** YOU'VE REGAINED FOCUS ** @Victim
    '3':
      chance: 19
      cooldown: 4
      effects:
      - POTION:CONFUSION:0:120 @Victim
      - HALF_DAMAGE
      - MESSAGE:§e§l** YOU'VE BEEN UNFOCUSED ** @Victim
      - WAIT:125
      - MESSAGE:§a§l** YOU'VE REGAINED FOCUS ** @Victim
    '4':
      chance: 25
      cooldown: 4
      effects:
      - POTION:CONFUSION:1:60 @Victim
      - HALF_DAMAGE
      - MESSAGE:§e§l** YOU'VE BEEN UNFOCUSED ** @Victim
      - WAIT:65
      - MESSAGE:§a§l** YOU'VE REGAINED FOCUS ** @Victim
    '5':
      chance: 32
      cooldown: 4
      effects:
      - POTION:CONFUSION:1:100 @Victim
      - HALF_DAMAGE
      - MESSAGE:§e§l** YOU'VE BEEN UNFOCUSED ** @Victim
      - WAIT:105
      - MESSAGE:§a§l** YOU'VE REGAINED FOCUS ** @Victim
valor:
  display: '%group-color%Valor'
  description: |-
    La oportunidad de reducir el daño entrante mientras
    empuñando una espada hasta en un 22% al nivel máximo.
  applies-to: ꐤ ꐞ ꐧ ꐥ
  type: DEFENSE
  group: ULTIMATE
  applies:
  - ALL_ARMOR
  levels:
    '1':
      chance: 4
      cooldown: 4
      conditions:
      - '%victim is holding% contains SWORD : %allow%'
      effects:
      - DECREASE_DAMAGE:<random number>1-4</random number> @Victim
    '2':
      chance: 9
      cooldown: 4
      conditions:
      - '%attacker is holding% contains SWORD : %allow%'
      effects:
      - DECREASE_DAMAGE:<random number>8-12</random number> @Victim
    '3':
      chance: 13
      cooldown: 4
      conditions:
      - '%attacker is holding% contains SWORD : %allow%'
      effects:
      - DECREASE_DAMAGE:<random number>12-15</random number> @Victim
    '4':
      chance: 16
      cooldown: 4
      conditions:
      - '%attacker is holding% contains SWORD : %allow%'
      effects:
      - DECREASE_DAMAGE:<random number>15-18</random number> @Victim
    '5':
      chance: 21
      cooldown: 4
      conditions:
      - '%attacker is holding% contains SWORD : %allow%'
      effects:
      - DECREASE_DAMAGE:<random number>18-22</random number> @Victim
pacify:
  display: '%group-color%Pacify'
  description: |-
    Una oportunidad de pacify su objetivo,
    infligiendo 1-4 de daño y
    deteniendo su próximo ataque contra ti.
  applies-to: ꐣ
  type: SHOOT;SHOOT_MOB
  group: ULTIMATE
  applies:
  - BOW
  - CROSSBOW
  levels:
    '1':
      chance: 12
      cooldown: 3
      effects:
      - CANCEL_EVENT
      - DO_HARM:<random number>1-4</random number> @Victim
    '2':
      chance: 18
      cooldown: 3
      effects:
      - CANCEL_EVENT
      - DO_HARM:<random number>1-4</random number> @Victim
    '3':
      chance: 24
      cooldown: 3
      effects:
      - CANCEL_EVENT
      - DO_HARM:<random number>1-4</random number> @Victim
    '4':
      chance: 30
      cooldown: 3
      effects:
      - CANCEL_EVENT
      - DO_HARM:<random number>1-4</random number> @Victim
metaphysical:
  display: '%group-color%Metaphysical'
  description: |-
    Una oportunidad de ser curado de
    Lentitud cuando se ataca.
    A nivel máximo, solo estarás
    afectado aprox.10% del tiempo.
  applies-to: ꐥ
  type: DEFENSE
  group: ULTIMATE
  applies:
  - ALL_BOOTS
  levels:
    '1':
      chance: 30
      effects:
      - CURE:SLOW @Victim
    '2':
      chance: 60
      effects:
      - CURE:SLOW @Victim
    '3':
      chance: 75
      effects:
      - CURE:SLOW @Victim
    '4':
      chance: 90
      effects:
      - CURE:SLOW @Victim
creeperarmor:
  display: '%group-color%Creeper Armor'
  description: |-
    Oportunidad de ser inmune a explosive daño, en
    niveles más altos tienes la oportunidad de sanar.
  applies-to: ꐤ ꐞ ꐧ ꐥ
  type: EXPLOSION
  group: ULTIMATE
  applies:
  - ALL_ARMOR
  levels:
    '1':
      chance: 25
      effects:
      - CANCEL_EVENT
    '2':
      chance: 50
      effects:
      - CANCEL_EVENT
    '3':
      chance: 75
      effects:
      - CANCEL_EVENT
      - ADD_HEALTH:<random number>1-2</random number>
spirits:
  display: '%group-color%Spirits'
  description: |-
    Oportunidad de engendrar ardientes que sanan
    tú mismo y tus aliados en combate.
  applies-to: ꐤ ꐞ ꐧ ꐥ
  type: DEFENSE
  group: ULTIMATE
  applies:
  - ALL_ARMOR
  levels:
    '1':
      chance: 2
      cooldown: 8
      effects:
      - GUARD:BLAZE:@Victim
      - GUARD:BLAZE:@Victim
      - GUARD:BLAZE:@Victim
      - POTION:REGENERATION:0:60 @Aoe{r=5,t=undamageable}
    '2':
      chance: 2
      cooldown: 8
      effects:
      - GUARD:BLAZE:@Victim
      - GUARD:BLAZE:@Victim
      - GUARD:BLAZE:@Victim
      - GUARD:BLAZE:@Victim
      - POTION:REGENERATION:0:60 @Aoe{r=5,t=undamageable}
    '3':
      chance: 3
      cooldown: 8
      effects:
      - GUARD:BLAZE:@Victim
      - GUARD:BLAZE:@Victim
      - GUARD:BLAZE:@Victim
      - GUARD:BLAZE:@Victim
      - POTION:REGENERATION:0:60 @Aoe{r=5,t=undamageable}
    '4':
      chance: 5
      cooldown: 8
      effects:
      - GUARD:BLAZE:@Victim
      - GUARD:BLAZE:@Victim
      - GUARD:BLAZE:@Victim
      - GUARD:BLAZE:@Victim
      - POTION:REGENERATION:0:60 @Aoe{r=5,t=undamageable}
    '5':
      chance: 8
      cooldown: 8
      effects:
      - GUARD:BLAZE:@Victim
      - GUARD:BLAZE:@Victim
      - GUARD:BLAZE:@Victim
      - GUARD:BLAZE:@Victim
      - POTION:REGENERATION:0:60 @Aoe{r=5,t=undamageable}
    '6':
      chance: 12
      cooldown: 8
      effects:
      - GUARD:BLAZE:@Victim
      - GUARD:BLAZE:@Victim
      - GUARD:BLAZE:@Victim
      - GUARD:BLAZE:@Victim
      - POTION:REGENERATION:0:60 @Aoe{r=5,t=undamageable}
    '7':
      chance: 15
      cooldown: 8
      effects:
      - GUARD:BLAZE:@Victim
      - GUARD:BLAZE:@Victim
      - GUARD:BLAZE:@Victim
      - GUARD:BLAZE:@Victim
      - POTION:REGENERATION:0:60 @Aoe{r=5,t=undamageable}
    '8':
      chance: 19
      cooldown: 8
      effects:
      - GUARD:BLAZE:@Victim
      - GUARD:BLAZE:@Victim
      - GUARD:BLAZE:@Victim
      - GUARD:BLAZE:@Victim
      - POTION:REGENERATION:0:60  @Aoe{r=5,t=undamageable}
    '9':
      chance: 22
      cooldown: 8
      effects:
      - GUARD:BLAZE:@Victim
      - GUARD:BLAZE:@Victim
      - GUARD:BLAZE:@Victim
      - GUARD:BLAZE:@Victim
      - POTION:REGENERATION:0:60  @Aoe{r=5,t=undamageable}
    '10':
      chance: 27
      cooldown: 8
      effects:
      - GUARD:BLAZE:@Victim
      - GUARD:BLAZE:@Victim
      - GUARD:BLAZE:@Victim
      - GUARD:BLAZE:@Victim
      - GUARD:BLAZE:@Victim
      - POTION:REGENERATION:0:60  @Aoe{r=5,t=undamageable}
bleed:
  display: '%group-color%Bleed'
  description: |-
    Se aplica efecto de sangrado a los enemigos
    que disminuyen su velocidad de movimiento.
  applies-to: ꐝ
  type: ATTACK
  group: ULTIMATE
  applies:
  - ALL_AXE
  levels:
    '1':
      chance: 8
      effects:
      - POTION:SLOW:0:100 @Victim
      - DO_HARM:<random number>1-3</random number> @Victim
      - MESSAGE:§4Sangrando! @Victim
      - WAIT:20
      - DO_HARM:<random number>1-3</random number> @Victim
      - WAIT:20
      - DO_HARM:<random number>1-3</random number> @Victim
    '2':
      chance: 15
      effects:
      - POTION:SLOW:0:100 @Victim
      - DO_HARM:<random number>1-3</random number> @Victim
      - MESSAGE:§4Sangrando! @Victim
      - WAIT:20
      - DO_HARM:<random number>1-3</random number> @Victim
      - WAIT:20
      - DO_HARM:<random number>1-3</random number> @Victim
    '3':
      chance: 23
      effects:
      - POTION:SLOW:1:100 @Victim
      - DO_HARM:<random number>1-3</random number> @Victim
      - MESSAGE:§4Sangrando! @Victim
      - WAIT:20
      - DO_HARM:<random number>1-3</random number> @Victim
      - WAIT:20
      - DO_HARM:<random number>1-3</random number> @Victim
    '4':
      chance: 30
      effects:
      - POTION:SLOW:1:100 @Victim
      - DO_HARM:<random number>1-3</random number> @Victim
      - MESSAGE:§4Sangrando! @Victim
      - WAIT:20
      - DO_HARM:<random number>1-3</random number> @Victim
      - WAIT:20
      - DO_HARM:<random number>1-3</random number> @Victim
    '5':
      chance: 44
      effects:
      - POTION:SLOW:1:100 @Victim
      - DO_HARM:<random number>1-3</random number> @Victim
      - MESSAGE:§4Sangrando! @Victim
      - WAIT:20
      - DO_HARM:<random number>1-3</random number> @Victim
      - WAIT:20
      - DO_HARM:<random number>1-3</random number> @Victim
    '6':
      chance: 60
      effects:
      - POTION:SLOW:2:100 @Victim
      - DO_HARM:<random number>1-3</random number> @Victim
      - MESSAGE:§4Sangrando! @Victim
      - WAIT:20
      - DO_HARM:<random number>1-3</random number> @Victim
      - WAIT:20
      - DO_HARM:<random number>1-3</random number> @Victim
lavawalker:
  display: '%group-color%Lava Walker'
  description: Camina sobre lava.
  applies-to: ꐥ
  type: EFFECT_STATIC
  group: LEGENDARY
  applies:
  - ALL_BOOTS
  levels:
    '1':
      effects:
      - LAVA_WALKER
impale:
  display: '%group-color%Impale'
  description: |-
    Oportunidad de causar grandes cantidades de daño a tu oponente, causando
    Sentura V por algún tiempo
  applies-to: ꐣ
  type: SHOOT
  group: LEGENDARY
  applies:
  - BOW
  - CROSSBOW
  levels:
    '1':
      chance: 4
      cooldown: 26
      effects:
      - DOUBLE_DAMAGE
      - POTION:SLOW:4:20 @Victim
    '2':
      chance: 6
      cooldown: 24
      effects:
      - DOUBLE_DAMAGE
      - POTION:SLOW:4:40 @Victim
    '3':
      chance: 8
      cooldown: 22
      effects:
      - DOUBLE_DAMAGE
      - POTION:SLOW:4:60 @Victim
    '4':
      chance: 10
      cooldown: 20
      effects:
      - DOUBLE_DAMAGE
      - POTION:SLOW:4:80 @Victim
protection:
  display: '%group-color%Protection'
  description: |-
    Cura y cura automáticamente
    Todos los aliados de facción cercanos.
  applies-to: ꐤ ꐞ ꐧ ꐥ
  type: DEFENSE
  group: LEGENDARY
  applies:
  - ALL_ARMOR
  levels:
    '1':
      chance: 6
      cooldown: 20
      effects:
      - ADD_HEALTH:2 @Aoe{r=5,t=undamageable}
      - CURE:POISON @Aoe{r=5,t=undamageable}
      - CURE:NAUSEA @Aoe{r=5,t=undamageable}
      - CURE:WITHER @Aoe{r=5,t=undamageable}
      - MESSAGE:§e§l*** §eProtection §e§l*** §7(%victim name%) @Aoe{r=5,t=undamageable}
    '2':
      chance: 7
      cooldown: 20
      effects:
      - ADD_HEALTH:3 @Aoe{r=6,t=undamageable}
      - CURE:POISON @Aoe{r=6,t=undamageable}
      - CURE:NAUSEA @Aoe{r=6,t=undamageable}
      - CURE:WITHER @Aoe{r=6,t=undamageable}
      - MESSAGE:§e§l*** §eProtection §e§l*** §7(%victim name%) 
      - CURE:WITHER @Aoe{r=6,t=undamageable}
    '3':
      chance: 8
      cooldown: 22
      effects:
      - ADD_HEALTH:4 @Aoe{r=7,t=undamageable}
      - CURE:POISON @Aoe{r=7,t=undamageable}
      - CURE:NAUSEA @Aoe{r=7,t=undamageable}
      - CURE:WITHER @Aoe{r=7,t=undamageable}
      - MESSAGE:§e§l*** §eProtection §e§l*** §7(%victim name%)  @Aoe{r=7,t=undamageable}
    '4':
      chance: 10
      cooldown: 22
      effects:
      - ADD_HEALTH:5 @Aoe{r=8,t=undamageable}
      - CURE:POISON @Aoe{r=8,t=undamageable}
      - CURE:NAUSEA @Aoe{r=8,t=undamageable}
      - CURE:WITHER @Aoe{r=8,t=undamageable}
      - MESSAGE:§e§l*** §eProtection §e§l*** §7(%victim name%) @Aoe{r=8,t=undamageable}
    '5':
      chance: 12
      cooldown: 25
      effects:
      - ADD_HEALTH:6 @Aoe{r=10,t=undamageable}
      - CURE:POISON @Aoe{r=10,t=undamageable}
      - CURE:NAUSEA @Aoe{r=10,t=undamageable}
      - CURE:WITHER @Aoe{r=10,t=undamageable}
      - MESSAGE:§e§l*** §eProtection §e§l*** §7(%victim name%) @Aoe{r=10,t=undamageable}
torrent:
  display: '%group-color%Torrent'
  description: Inflige un mayor daño mientras está en el agua.
  applies-to: ꐥ
  type: ATTACK
  group: LEGENDARY
  applies:
  - ALL_BOOTS
  levels:
    '1':
      chance: 8
      cooldown: 3
      conditions:
      - '%is under water% = TRUE : %allow%'
      effects:
      - DOUBLE_DAMAGE
    '2':
      chance: 13
      cooldown: 3
      conditions:
      - '%is under water% = TRUE : %allow%'
      effects:
      - DOUBLE_DAMAGE
    '3':
      chance: 19
      cooldown: 5
      conditions:
      - '%is under water% = TRUE : %allow%'
      effects:
      - DOUBLE_DAMAGE
    '4':
      chance: 23
      cooldown: 5
      conditions:
      - '%is under water% = TRUE : %allow%'
      effects:
      - DOUBLE_DAMAGE
judgement:
  display: '%group-color%Judgement'
  description: |-
    Posibilidad de tratar poison daño a
    su objetivo y agregar regeneración a ti mismo.
  applies-to: ꐤ ꐞ ꐧ ꐥ
  type: DEFENSE
  group: LEGENDARY
  applies:
  - ALL_ARMOR
  levels:
    '1':
      chance: 6
      cooldown: 20
      effects:
      - POTION:POISON:0:100 @Attacker
      - POTION:REGENERATION:0:100 @Victim
    '2':
      chance: 8
      cooldown: 20
      effects:
      - POTION:POISON:0:100 @Attacker
      - POTION:REGENERATION:0:100 @Victim
    '3':
      chance: 10
      cooldown: 20
      effects:
      - POTION:POISON:0:100 @Attacker
      - POTION:REGENERATION:0:100 @Victim
    '4':
      chance: 12
      cooldown: 20
      effects:
      - POTION:POISON:0:100 @Attacker
      - POTION:REGENERATION:1:60 @Victim
    '5':
      chance: 16
      cooldown: 25
      effects:
      - POTION:POISON:0:100 @Attacker
      - POTION:REGENERATION:1:100 @Victim
surprise:
  display: '%group-color%Surprise'
  description: |-
    Oportunidad de teletransportar detrás de tu oponente
    y tómalos por surprise.
  applies-to: ꐤ ꐞ ꐧ ꐥ
  type: DEFENSE
  group: LEGENDARY
  applies:
  - ALL_ARMOR
  levels:
    '1':
      chance: 8
      cooldown: 5
      effects:
      - MESSAGE:§6§l** SURPRISE ** @Victim
      - TELEPORT_BEHIND @Victim
    '2':
      chance: 14
      cooldown: 5
      effects:
      - MESSAGE:§6§l** SURPRISE ** @Victim
      - TELEPORT_BEHIND @Victim
    '3':
      chance: 17
      cooldown: 5
      effects:
      - MESSAGE:§6§l** SURPRISE ** @Victim
      - TELEPORT_BEHIND @Victim
    '4':
      chance: 21
      cooldown: 5
      effects:
      - MESSAGE:§6§l** SURPRISE ** @Victim
      - TELEPORT_BEHIND @Victim
stun:
  display: '%group-color%Stun'
  description: |-
    Oportunidad de ralentizar el oponente, hacerlos
    Siéntete débil y quita la lentitud de ti.
  applies-to: ꐚ ꐝ
  type: ATTACK
  group: LEGENDARY
  applies:
  - ALL_AXE
  - ALL_SWORD
  levels:
    '1':
      chance: 15
      cooldown: 6
      effects:
      - POTION:SLOW:0:120 @Victim
      - CURE:SLOW @Attacker
      - CURE_PERMANENT:SLOW @Attacker
      - POTION:WEAKNESS:0:80 @Victim
      - MESSAGE:§c§l** STUNNED ** @Victim
    '2':
      chance: 23
      cooldown: 6
      effects:
      - POTION:SLOW:0:120 @Victim
      - CURE:SLOW @Attacker
      - CURE_PERMANENT:SLOW @Attacker
      - POTION:WEAKNESS:0:80 @Victim
      - MESSAGE:§c§l** STUNNED ** @Victim
    '3':
      chance: 35
      cooldown: 6
      effects:
      - POTION:SLOW:1:120 @Victim
      - CURE:SLOW @Attacker
      - CURE_PERMANENT:SLOW @Attacker
      - POTION:WEAKNESS:0:80 @Victim
      - MESSAGE:§c§l** STUNNED ** @Victim
unholy:
  display: '%group-color%Unholy'
  description: Oportunidad de dar debilidad y wither a tu atacante.
  applies-to: ꐤ ꐞ ꐧ ꐥ
  type: DEFENSE
  group: LEGENDARY
  applies:
  - ALL_ARMOR
  levels:
    '1':
      chance: 2
      cooldown: 40
      effects:
      - POTION:WITHER:0:60 @Attacker
      - POTION:WEAKNESS:0:100 @Attacker
    '2':
      chance: 4
      cooldown: 40
      effects:
      - POTION:WITHER:1:60 @Attacker
      - POTION:WEAKNESS:0:5 @Attacker
    '3':
      chance: 6
      cooldown: 40
      effects:
      - POTION:WITHER:1:60 @Attacker
      - POTION:WEAKNESS:0:100 @Attacker
    '4':
      chance: 8
      cooldown: 40
      effects:
      - POTION:WITHER:1:60 @Attacker
      - POTION:WEAKNESS:0:100 @Attacker
    '5':
      chance: 10
      cooldown: 40
      effects:
      - POTION:WITHER:1:60 @Attacker
      - POTION:WEAKNESS:0:100 @Attacker
quiver:
  display: '%group-color%Quiver'
  description: Oportunidad de arrojar a tus atacantes al aire.
  applies-to: ꐥ
  type: DEFENSE
  group: LEGENDARY
  applies:
  - ALL_BOOTS
  levels:
    '1':
      chance: 8
      cooldown: 10
      effects:
      - PULL_AWAY:1
    '2':
      chance: 10
      cooldown: 10
      effects:
      - PULL_AWAY:1.5
    '3':
      chance: 12
      cooldown: 10
      effects:
      - PULL_AWAY:2
    '4':
      chance: 14
      cooldown: 10
      effects:
      - PULL_AWAY:2.5
    '5':
      chance: 16
      cooldown: 10
      effects:
      - PULL_AWAY:3
    '6':
      chance: 18
      cooldown: 10
      effects:
      - PULL_AWAY:3.5
fat:
  display: '%group-color%Fat'
  description: |-
    La posibilidad de recibir una mayor negación de daños
    cuando se daña, así como la absorción en niveles más altos.
  applies-to: ꐧ
  type: DEFENSE
  group: LEGENDARY
  applies:
  - ALL_CHESTPLATE
  levels:
    '1':
      chance: 5
      cooldown: 10
      effects:
      - NEGATE_DAMAGE:10 @Victim
      - MESSAGE:§6§l** FAT ** @Victim
    '2':
      chance: 10
      cooldown: 10
      effects:
      - NEGATE_DAMAGE:20 @Victim
      - MESSAGE:§6§l** FAT ** @Victim
    '3':
      chance: 12
      cooldown: 10
      effects:
      - NEGATE_DAMAGE:30 @Victim
      - MESSAGE:§6§l** FAT ** @Victim
      - POTION:ABSORPTION:3:60 @Victim
    '4':
      chance: 15
      cooldown: 10
      effects:
      - NEGATE_DAMAGE:40 @Victim
      - MESSAGE:§6§l** FAT ** @Victim
      - POTION:ABSORPTION:4:80 @Victim
    '5':
      chance: 18
      cooldown: 10
      effects:
      - NEGATE_DAMAGE:50 @Victim
      - MESSAGE:§6§l** FAT ** @Victim
      - POTION:ABSORPTION:4:80 @Victim
    '6':
      chance: 20
      cooldown: 10
      effects:
      - NEGATE_DAMAGE:60 @Victim
      - MESSAGE:§6§l** FAT ** @Victim
      - POTION:ABSORPTION:5:100 @Victim
hex:
  display: '%group-color%Hex'
  description: |-
    Una vez que un objetivo se ve afectado por Hex,
    Una parte de todo su daño saliente disminuye.
    3-7 El daño se refleja en ellos.
  applies-to: ꐝ
  type: ATTACK
  group: LEGENDARY
  applies:
  - ALL_AXE
  levels:
    '1':
      chance: 8
      cooldown: 4
      effects:
      - DECREASE_DAMAGE:<random number>10-50</random number> @Attacker
      - DO_HARM:<random number>3-7</random number> @Victim
    '2':
      chance: 15
      cooldown: 4
      effects:
      - DECREASE_DAMAGE:<random number>10-50</random number> @Attacker
      - DO_HARM:<random number>3-7</random number> @Victim
    '3':
      chance: 19
      cooldown: 4
      effects:
      - DECREASE_DAMAGE:<random number>10-50</random number> @Attacker
      - DO_HARM:<random number>3-7</random number> @Victim
    '4':
      chance: 25
      cooldown: 4
      effects:
      - DECREASE_DAMAGE:<random number>10-50</random number> @Attacker
      - DO_HARM:<random number>3-7</random number> @Victim
barbarian:
  display: '%group-color%Barbarian'
  description: La oportunidad de infligir más daño en el hacha.
  applies-to: ꐝ
  type: ATTACK
  group: LEGENDARY
  applies:
  - ALL_AXE
  levels:
    '1':
      chance: 8
      cooldown: 2
      conditions:
      - '%attacker is holding% contains AXE : %allow%'
      effects:
      - INCREASE_DAMAGE:<random number>25-100</random number> @Victim
    '2':
      chance: 15
      cooldown: 2
      conditions:
      - '%attacker is holding% contains AXE : %allow%'
      effects:
      - INCREASE_DAMAGE:<random number>25-100</random number> @Victim
    '3':
      chance: 19
      cooldown: 2
      conditions:
      - '%attacker is holding% contains AXE : %allow%'
      effects:
      - INCREASE_DAMAGE:<random number>25-100</random number> @Victim
    '4':
      chance: 25
      cooldown: 2
      conditions:
      - '%attacker is holding% contains AXE : %allow%'
      effects:
      - INCREASE_DAMAGE:<random number>25-100</random number> @Victim
clarity:
  display: '%group-color%Clarity'
  description: Cure la ceguera cuando se ataca.
  applies-to: ꐤ ꐞ ꐧ ꐥ
  type: DEFENSE
  group: LEGENDARY
  applies:
  - ALL_ARMOR
  levels:
    '1':
      effects:
      - CURE:BLINDNESS @Victim
    '2':
      effects:
      - CURE:BLINDNESS @Victim
    '3':
      effects:
      - CURE:BLINDNESS @Victim
deathbringer:
  display: '%group-color%Deathbringer'
  description: Oportunidad de causar doble daño.
  applies-to: ꐤ ꐞ ꐧ ꐥ
  type: ATTACK
  group: LEGENDARY
  applies:
  - ALL_ARMOR
  levels:
    '1':
      chance: 15.8
      cooldown: 45
      effects:
      - DOUBLE_DAMAGE
    '2':
      chance: 22.1
      cooldown: 45
      effects:
      - DOUBLE_DAMAGE
    '3':
      chance: 28
      cooldown: 45
      effects:
      - DOUBLE_DAMAGE
doublestrike:
  display: '%group-color%Double Strike'
  description: Una oportunidad de strike dos veces.
  applies-to: ꐚ
  type: ATTACK
  group: LEGENDARY
  applies:
  - ALL_SWORD
  levels:
    '1':
      chance: 8
      cooldown: 15
      effects:
      - WAIT:20
      - DO_HARM:%damage% @Victim
      - MESSAGE:§6§l** DOUBLE STRIKE ** @Victim
    '2':
      chance: 13
      cooldown: 15
      effects:
      - WAIT:20
      - DO_HARM:%damage% @Victim
      - MESSAGE:§6§l** DOUBLE STRIKE ** @Victim
    '3':
      chance: 19
      cooldown: 15
      effects:
      - WAIT:20
      - DO_HARM:%damage% @Victim
      - MESSAGE:§6§l** DOUBLE STRIKE ** @Victim
drunk:
  display: '%group-color%Drunk'
  description: |-
    Lentitud y balanceo lento con
    una oportunidad para obtener fuerza.
  applies-to: ꐤ
  type: EFFECT_STATIC
  group: LEGENDARY
  applies:
  - ALL_HELMET
  levels:
    '1':
      effects:
      - POTION:SLOW_DIGGING:0
      - POTION:INCREASE_DAMAGE:0
      - POTION:SLOW:0
    '2':
      effects:
      - POTION:SLOW_DIGGING:0
      - POTION:INCREASE_DAMAGE:0
      - POTION:SLOW:0
    '3':
      effects:
      - POTION:SLOW_DIGGING:1
      - POTION:INCREASE_DAMAGE:1
      - POTION:SLOW:1
    '4':
      effects:
      - POTION:SLOW_DIGGING:2
      - POTION:INCREASE_DAMAGE:2
      - POTION:SLOW:2
enlighted:
  display: '%group-color%Enlighted'
  description: Puede sanar corazones mientras recibe daño.
  applies-to: ꐤ ꐞ ꐧ ꐥ
  type: DEFENSE
  group: LEGENDARY
  applies:
  - ALL_ARMOR
  levels:
    '1':
      chance: 6
      cooldown: 30
      effects:
      - ADD_HEALTH:<random number>1-3</random number> @Victim
    '2':
      chance: 9
      cooldown: 30
      effects:
      - ADD_HEALTH:<random number>1-3</random number> @Victim
    '3':
      chance: 12
      cooldown: 30
      effects:
      - ADD_HEALTH:<random number>1-3</random number> @Victim
gears:
  display: '%group-color%Gears'
  description: Velocidad agregada cuando está equipado.
  applies-to: ꐥ
  type: EFFECT_STATIC
  group: LEGENDARY
  applies:
  - ALL_BOOTS
  levels:
    '1':
      effects:
      - POTION:SPEED:0
    '2':
      effects:
      - POTION:SPEED:1
    '3':
      effects:
      - POTION:SPEED:2
killaura:
  display: '%group-color%Kill Aura'
  description: Oportunidad de matar múltiples monstruos \ en una pila cada evento de muerte.
  applies-to: ꐚ
  group: LEGENDARY
  type: ATTACK_MOB
  applies:
  - ALL_SWORD
  levels:
    '1':
      chance: 5
      cooldown: 3
      effects:
      - KILL:<random number>2-3</random number> @Victim
    '2':
      chance: 8
      cooldown: 4
      effects:
      - KILL:<random number>2-4</random number> @Victim
    '3':
      chance: 12
      cooldown: 5
      effects:
      - KILL:<random number>2-4</random number> @Victim
    '4':
      chance: 15
      cooldown: 5
      effects:
      - KILL:<random number>2-5</random number> @Victim
    '5':
      chance: 18
      cooldown: 6
      effects:
      - KILL:<random number>3-5</random number> @Victim
inquisitive:
  display: '%group-color%Inquisitive'
  description: Oportunidad de aumentar las caídas de EXP de los monstruos.
  applies-to: ꐚ
  type: KILL_MOB
  group: LEGENDARY
  applies:
  - ALL_SWORD
  levels:
    '1':
      chance: 30
      cooldown: 4
      effects:
      - EXP:<math>%exp% * (1.0 + 0.25 * %level%)</math> @Victim
    '2':
      chance: 35
      cooldown: 4
      effects:
      - EXP:<math>%exp% * (1.0 + 0.25 * %level%)</math> @Victim
    '3':
      chance: 40
      cooldown: 4
      effects:
      - EXP:<math>%exp% * (1.0 + 0.25 * %level%)</math> @Victim
    '4':
      chance: 45
      cooldown: 4
      effects:
      - EXP:<math>%exp% * (1.0 + 0.25 * %level%)</math> @Victim
inversion:
  display: '%group-color%Inversion'
  description: |-
    El daño que se le da la oportunidad tiene la oportunidad de ser
    Bloqueado y curado por 1-5 hp.
  applies-to: ꐚ
  type: DEFENSE
  group: LEGENDARY
  applies:
  - ALL_SWORD
  levels:
    '1':
      chance: 8
      cooldown: 4
      effects:
      - CANCEL_EVENT
      - ADD_HEALTH:<random number>1-5</random number> @Victim
    '2':
      chance: 12
      cooldown: 4
      effects:
      - CANCEL_EVENT
      - ADD_HEALTH:<random number>1-5</random number> @Victim
    '3':
      chance: 16
      cooldown: 4
      effects:
      - CANCEL_EVENT
      - ADD_HEALTH:<random number>1-5</random number> @Victim
    '4':
      chance: 24
      cooldown: 4
      effects:
      - CANCEL_EVENT
      - ADD_HEALTH:<random number>1-5</random number> @Victim
lifesteal:
  display: '%group-color%Lifesteal'
  description: |-
    Una oportunidad para robar salud cuando
    agresor.
  applies-to: ꐚ
  type: ATTACK
  group: LEGENDARY
  applies:
  - ALL_SWORD
  levels:
    '1':
      chance: 9
      cooldown: 15
      effects:
      - STEAL_HEALTH:<random number>1-3</random number> @Attacker
    '2':
      chance: 13
      cooldown: 15
      effects:
      - STEAL_HEALTH:<random number>1-3</random number> @Attacker
    '3':
      chance: 17
      cooldown: 15
      effects:
      - STEAL_HEALTH:<random number>1-4</random number> @Attacker
    '4':
      chance: 21
      cooldown: 15
      effects:
      - STEAL_HEALTH:<random number>1-5</random number> @Attacker
    '5':
      chance: 25
      cooldown: 15
      effects:
      - STEAL_HEALTH:<random number>1-5</random number> @Attacker
overload:
  display: '%group-color%Overload'
  description: Aumento permanente en los corazones.
  applies-to: ꐤ ꐞ ꐧ ꐥ
  type: EFFECT_STATIC
  group: LEGENDARY
  applies:
  - ALL_ARMOR
  levels:
    '1':
      effects:
      - POTION:HEALTH_BOOST:0
    '2':
      effects:
      - POTION:HEALTH_BOOST:1
    '3':
      effects:
      - POTION:HEALTH_BOOST:2
rage:
  display: '%group-color%Rage'
  description: |-
    Por cada combo golpear tu tierra,
    oportunidad de hacer 0.5 daños cardíacos por combo
    a tu oponente.
    Hasta 5 éxitos combinados máximos.
  applies-to: ꐚ ꐝ
  type: ATTACK
  group: LEGENDARY
  applies:
  - ALL_AXE
  - ALL_SWORD
  levels:
    '1':
      chance: 25
      conditions:
      - '%attacker combo% > 5 : %stop%'
      cooldown: 10
      effects:
      - DO_HARM:%combo% @Victim
      - BLOOD @Victim
    '2':
      chance: 30
      conditions:
      - '%attacker combo% > 5 : %stop%'
      cooldown: 10
      effects:
      - DO_HARM:%combo% @Victim
      - BLOOD @Victim
    '3':
      chance: 35
      conditions:
      - '%attacker combo% > 5 : %stop%'
      cooldown: 10
      effects:
      - DO_HARM:%combo% @Victim
      - BLOOD @Victim
    '4':
      chance: 40
      conditions:
      - '%attacker combo% > 5 : %stop%'
      cooldown: 10
      effects:
      - DO_HARM:%combo% @Victim
      - BLOOD @Victim
    '5':
      chance: 45
      conditions:
      - '%attacker combo% > 5 : %stop%'
      cooldown: 10
      effects:
      - DO_HARM:%combo% @Victim
      - BLOOD @Victim
    '6':
      chance: 50
      conditions:
      - '%attacker combo% > 5 : %stop%'
      cooldown: 10
      effects:
      - DO_HARM:%combo% @Victim
      - BLOOD @Victim
silence:
  display: '%group-color%Silence'
  description: Oportunidad de detener la activación de los encantamientos de armadura personalizados de tu enemigo.
  applies-to: ꐚ
  type: ATTACK
  group: LEGENDARY
  applies:
  - ALL_SWORD
  levels:
    '1':
      chance: 1.8
      cooldown: 5
      effects:
      - DISABLE_ACTIVATION:endershift:3 @Victim
      - DISABLE_ACTIVATION:molten:3 @Victim
      - DISABLE_ACTIVATION:selfdestruct:3 @Victim
      - DISABLE_ACTIVATION:plaguecarrier:3 @Victim
      - DISABLE_ACTIVATION:ragdoll:3 @Victim
      - DISABLE_ACTIVATION:trickster:3 @Victim
      - DISABLE_ACTIVATION:smokebomb:3 @Victim
      - DISABLE_ACTIVATION:undeadruse:3 @Victim
      - DISABLE_ACTIVATION:voodoo:3 @Victim
      - DISABLE_ACTIVATION:cactus:3 @Victim
      - DISABLE_ACTIVATION:shockwave:3 @Victim
      - DISABLE_ACTIVATION:hardened:3 @Victim
      - DISABLE_ACTIVATION:wither:3 @Victim
      - DISABLE_ACTIVATION:tank:3 @Victim
      - DISABLE_ACTIVATION:valor:3 @Victim
      - DISABLE_ACTIVATION:dodge:3 @Victim
      - DISABLE_ACTIVATION:guardians:3 @Victim
      - DISABLE_ACTIVATION:heavy:3 @Victim
      - DISABLE_ACTIVATION:marksman:3 @Victim
      - DISABLE_ACTIVATION:diminish:3 @Victim
      - DISABLE_ACTIVATION:deathbringer:3 @Victim
      - DISABLE_ACTIVATION:armored:3 @Victim
      - DISABLE_ACTIVATION:enlighted:3 @Victim
      - DISABLE_ACTIVATION:deathgod:3 @Victim
      - DISABLE_ACTIVATION:planetarydeathbringer:3 @Victim
      - DISABLE_ACTIVATION:divineenlighted:3 @Victim
      - DISABLE_ACTIVATION:vengefuldiminish:3 @Victim
      - DISABLE_ACTIVATION:etherealdodge:3 @Victim
      - DISABLE_ACTIVATION:paladinarmored:3 @Victim
      - MESSAGE:§5§l* SILENCED§r §7[3s] §5§l* @Victim
    '2':
      chance: 2.5
      cooldown: 5
      effects:
      - DISABLE_ACTIVATION:endershift:3 @Victim
      - DISABLE_ACTIVATION:molten:3 @Victim
      - DISABLE_ACTIVATION:selfdestruct:3 @Victim
      - DISABLE_ACTIVATION:plaguecarrier:3 @Victim
      - DISABLE_ACTIVATION:ragdoll:3 @Victim
      - DISABLE_ACTIVATION:trickster:3 @Victim
      - DISABLE_ACTIVATION:arrowdeflect:3 @Victim
      - DISABLE_ACTIVATION:arrowbreak:3 @Victim
      - DISABLE_ACTIVATION:metaphysical:3 @Victim
      - DISABLE_ACTIVATION:tank:3 @Victim
      - DISABLE_ACTIVATION:valor:3 @Victim
      - DISABLE_ACTIVATION:dodge:3 @Victim
      - DISABLE_ACTIVATION:guardians:3 @Victim
      - DISABLE_ACTIVATION:heavy:3 @Victim
      - DISABLE_ACTIVATION:marksman:3 @Victim
      - DISABLE_ACTIVATION:diminish:3 @Victim
      - DISABLE_ACTIVATION:deathbringer:3 @Victim
      - DISABLE_ACTIVATION:armored:3 @Victim
      - DISABLE_ACTIVATION:enlighted:3 @Victim
      - DISABLE_ACTIVATION:deathgod:3 @Victim
      - DISABLE_ACTIVATION:planetarydeathbringer:3 @Victim
      - DISABLE_ACTIVATION:divineenlighted:3 @Victim
      - DISABLE_ACTIVATION:vengefuldiminish:3 @Victim
      - DISABLE_ACTIVATION:etherealdodge:3 @Victim
      - DISABLE_ACTIVATION:paladinarmored:3 @Victim
      - MESSAGE:§5§l* SILENCED§r §7[3s] §5§l* @Victim
    '3':
      chance: 2.9
      cooldown: 5
      effects:
      - DISABLE_ACTIVATION:endershift:5 @Victim
      - DISABLE_ACTIVATION:molten:5 @Victim
      - DISABLE_ACTIVATION:selfdestruct:5 @Victim
      - DISABLE_ACTIVATION:plaguecarrier:5 @Victim
      - DISABLE_ACTIVATION:angelic:5 @Victim
      - DISABLE_ACTIVATION:spirits:5 @Victim
      - DISABLE_ACTIVATION:arrowdeflect:5 @Victim
      - DISABLE_ACTIVATION:arrowbreak:5 @Victim
      - DISABLE_ACTIVATION:metaphysical:5 @Victim
      - DISABLE_ACTIVATION:tank:5 @Victim
      - DISABLE_ACTIVATION:valor:5 @Victim
      - DISABLE_ACTIVATION:dodge:5 @Victim
      - DISABLE_ACTIVATION:guardians:5 @Victim
      - DISABLE_ACTIVATION:heavy:5 @Victim
      - DISABLE_ACTIVATION:marksman:5 @Victim
      - DISABLE_ACTIVATION:diminish:5 @Victim
      - DISABLE_ACTIVATION:deathbringer:5 @Victim
      - DISABLE_ACTIVATION:armored:5 @Victim
      - DISABLE_ACTIVATION:enlighted:5 @Victim
      - DISABLE_ACTIVATION:deathgod:5 @Victim
      - DISABLE_ACTIVATION:planetarydeathbringer:5 @Victim
      - DISABLE_ACTIVATION:divineenlighted:5 @Victim
      - DISABLE_ACTIVATION:vengefuldiminish:5 @Victim
      - DISABLE_ACTIVATION:etherealdodge:5 @Victim
      - DISABLE_ACTIVATION:paladinarmored:5 @Victim
      - MESSAGE:§5§l* SILENCED§r §7[5s] §5§l* @Victim
    '4':
      chance: 3.1
      cooldown: 5
      effects:
      - DISABLE_ACTIVATION:endershift:7 @Victim
      - DISABLE_ACTIVATION:molten:7 @Victim
      - DISABLE_ACTIVATION:selfdestruct:7 @Victim
      - DISABLE_ACTIVATION:plaguecarrier:7 @Victim
      - DISABLE_ACTIVATION:ragdoll:7 @Victim
      - DISABLE_ACTIVATION:spirits:7 @Victim
      - DISABLE_ACTIVATION:arrowdeflect:7 @Victim
      - DISABLE_ACTIVATION:arrowbreak:7 @Victim
      - DISABLE_ACTIVATION:metaphysical:7 @Victim
      - DISABLE_ACTIVATION:tank:7 @Victim
      - DISABLE_ACTIVATION:valor:7 @Victim
      - DISABLE_ACTIVATION:dodge:7 @Victim
      - DISABLE_ACTIVATION:guardians:7 @Victim
      - DISABLE_ACTIVATION:heavy:7 @Victim
      - DISABLE_ACTIVATION:marksman:7 @Victim
      - DISABLE_ACTIVATION:diminish:7 @Victim
      - DISABLE_ACTIVATION:deathbringer:7 @Victim
      - DISABLE_ACTIVATION:armored:7 @Victim
      - DISABLE_ACTIVATION:enlighted:7 @Victim
      - DISABLE_ACTIVATION:deathgod:7 @Victim
      - DISABLE_ACTIVATION:planetarydeathbringer:7 @Victim
      - DISABLE_ACTIVATION:divineenlighted:7 @Victim
      - DISABLE_ACTIVATION:vengefuldiminish:7 @Victim
      - DISABLE_ACTIVATION:etherealdodge:7 @Victim
      - DISABLE_ACTIVATION:paladinarmored:7 @Victim
      - MESSAGE:§5§l* SILENCED§r §7[7s] §5§l* @Victim
armored:
  display: '%group-color%Armored'
  description: |-
    Disminuye el daño del enemigo
    Espadas por un 2% por nivel.
  applies-to: ꐤ ꐞ ꐧ ꐥ
  type: DEFENSE
  group: LEGENDARY
  applies:
  - ALL_ARMOR
  levels:
    '1':
      chance: 6
      cooldown: 8
      conditions:
      - '%attacker is holding% contains SWORD : %allow%'
      effects:
      - DECREASE_DAMAGE:2 @Attacker
    '2':
      chance: 12
      cooldown: 8
      conditions:
      - '%attacker is holding% contains SWORD : %allow%'
      effects:
      - DECREASE_DAMAGE:4 @Attacker
    '3':
      chance: 16
      cooldown: 8
      conditions:
      - '%attacker is holding% contains SWORD : %allow%'
      effects:
      - DECREASE_DAMAGE:6 @Attacker
    '4':
      chance: 20
      cooldown: 8
      conditions:
      - '%attacker is holding% contains SWORD : %allow%'
      effects:
      - DECREASE_DAMAGE:8 @Attacker
exterminator:
  display: '%group-color%Exterminator'
  description: |-
    Cuando se ataca, la oportunidad de deshabilitar temporalmente
    habilidad enemiga para usar un vivienda viviente, guardianes,
    y espíritus.
  applies-to: ꐞ
  type: DEFENSE
  group: LEGENDARY
  applies:
  - ALL_LEGGINGS
  levels:
    '1':
      chance: 6
      cooldown: 13
      effects:
      - DISABLE_ACTIVATION:undeadruse:4 @Attacker
      - DISABLE_ACTIVATION:guardians:4 @Attacker
      - DISABLE_ACTIVATION:spirits:4 @Attacker
    '2':
      chance: 12
      cooldown: 13
      effects:
      - DISABLE_ACTIVATION:undeadruse:6 @Attacker
      - DISABLE_ACTIVATION:guardians:6 @Attacker
      - DISABLE_ACTIVATION:spirits:6 @Attacker
    '3':
      chance: 18
      cooldown: 13
      effects:
      - DISABLE_ACTIVATION:undeadruse:8 @Attacker
      - DISABLE_ACTIVATION:guardians:8 @Attacker
      - DISABLE_ACTIVATION:spirits:8 @Attacker
blacksmith:
  display: '%group-color%Blacksmith'
  description: |-
    Oportunidad de sanar tu más dañado
    trozo de armadura por 1-2 durabilidad siempre que
    Golpeas a un jugador, pero cuando procesa tu
    El ataque solo abordará el 50% de la
    daño normal.
  applies-to: ꐝ
  type: ATTACK
  group: LEGENDARY
  applies:
  - ALL_AXE
  levels:
    '1':
      chance: 9
      cooldown: 3
      effects:
      - ADD_DURABILITY_ARMOR:-1
      - HALF_DAMAGE
      - MESSAGE:§6§l** BLACKSMITH ** @Attacker
    '2':
      chance: 15
      cooldown: 3
      effects:
      - ADD_DURABILITY_ARMOR:-1
      - HALF_DAMAGE
      - MESSAGE:§6§l** BLACKSMITH ** @Attacker
    '3':
      chance: 23
      cooldown: 3
      effects:
      - ADD_DURABILITY_ARMOR:-1
      - HALF_DAMAGE
      - MESSAGE:§6§l** BLACKSMITH ** @Attacker
    '4':
      chance: 31
      cooldown: 3
      effects:
      - ADD_DURABILITY_ARMOR:-2
      - HALF_DAMAGE
      - MESSAGE:§6§l** BLACKSMITH ** @Attacker
    '5':
      chance: 39
      cooldown: 3
      effects:
      - ADD_DURABILITY_ARMOR:-2
      - HALF_DAMAGE
      - MESSAGE:§6§l** BLACKSMITH ** @Attacker
abiding:
  display: '%group-color%Abiding'
  description: Las herramientas con este encantador se vuelven inquebrantables
  applies-to: ꐝ ꐜ ꐢ
  type: MINING;ATTACK;ATTACK_MOB
  group: LEGENDARY
  applies:
  - ALL_PICKAXE
  - ALL_SPADE
  - ALL_AXE
  levels:
    '1':
      effects:
      - REPAIR
devour:
  display: '%group-color%Devour'
  description: |-
    Oportunidad de multiplicar el daño tratado a
    Jugadores con pilas activas bleed.
  applies-to: ꐝ
  type: ATTACK
  group: LEGENDARY
  applies:
  - ALL_AXE
  levels:
    '1':
      chance: 25
      cooldown: 3
      conditions:
      - '%victim is bleeding% = false : %stop%'
      effects:
      - EXTRA_DAMAGE:<random number>1-4</random number>
    '2':
      chance: 40
      cooldown: 3
      conditions:
      - '%victim is bleeding% = false : %stop%'
      effects:
      - EXTRA_DAMAGE:<random number>1-4</random number>
    '3':
      chance: 55
      cooldown: 3
      conditions:
      - '%victim is bleeding% = false : %stop%'
      effects:
      - EXTRA_DAMAGE:<random number>1-4</random number>
    '4':
      chance: 75
      cooldown: 3
      conditions:
      - '%victim is bleeding% = false : %stop%'
      effects:
      - EXTRA_DAMAGE:<random number>1-4</random number>
diminish:
  display: '%group-color%Diminish'
  description: |-
    Cuando este efecto supere, el próximo ataque
    tratado con usted no puede tratar más de
    la (cantidad total de daño / 2)
    Tomaste del ataque anterior.
  applies-to: ꐧ
  type: DEFENSE
  group: LEGENDARY
  applies:
  - ALL_CHESTPLATE
  levels:
    '1':
      chance: 4
      cooldown: 8
      effects:
      - HALF_DAMAGE
    '2':
      chance: 8
      cooldown: 8
      effects:
      - HALF_DAMAGE
    '3':
      chance: 11
      cooldown: 8
      effects:
      - HALF_DAMAGE
    '4':
      chance: 15
      cooldown: 8
      effects:
      - HALF_DAMAGE
    '5':
      chance: 18
      cooldown: 8
      effects:
      - HALF_DAMAGE
    '6':
      chance: 23
      cooldown: 8
      effects:
      - HALF_DAMAGE
disarmor:
  display: '%group-color%Disarmor'
  description: |-
    Una ligera probabilidad de quitar uno
    pedazo de armadura de tu enemigo
    Cuando tienen baja salud.
  applies-to: ꐚ
  type: ATTACK
  group: LEGENDARY
  applies:
  - ALL_SWORD
  levels:
    '1':
      chance: 0.4
      cooldown: 6
      effects:
      - REMOVE_RANDOM_ARMOR @Victim
      - MESSAGE:§6§l** YOU HAVE BEEN DISARMORED ** @Victim
    '2':
      chance: 0.8
      cooldown: 6
      effects:
      - REMOVE_RANDOM_ARMOR @Victim
      - MESSAGE:§6§l** YOU HAVE BEEN DISARMORED ** @Victim
    '3':
      chance: 1.0
      cooldown: 6
      effects:
      - REMOVE_RANDOM_ARMOR @Victim
      - MESSAGE:§6§l** YOU HAVE BEEN DISARMORED ** @Victim
    '4':
      chance: 1.2
      cooldown: 6
      effects:
      - REMOVE_RANDOM_ARMOR @Victim
      - MESSAGE:§6§l** YOU HAVE BEEN DISARMORED ** @Victim
    '5':
      chance: 1.4
      cooldown: 6
      effects:
      - REMOVE_RANDOM_ARMOR @Victim
      - MESSAGE:§6§l** YOU HAVE BEEN DISARMORED ** @Victim
    '6':
      chance: 1.6
      cooldown: 6
      effects:
      - REMOVE_RANDOM_ARMOR @Victim
      - MESSAGE:§6§l** YOU HAVE BEEN DISARMORED ** @Victim
    '7':
      chance: 1.8
      cooldown: 6
      effects:
      - REMOVE_RANDOM_ARMOR @Victim
      - MESSAGE:§6§l** YOU HAVE BEEN DISARMORED ** @Victim
    '8':
      chance: 2
      cooldown: 6
      effects:
      - REMOVE_RANDOM_ARMOR @Victim
      - MESSAGE:§6§l** YOU HAVE BEEN DISARMORED ** @Victim
deathgod:
  display: '%group-color%Death God'
  description: |-
    Ataques que traen tu HP a
    (nivel+4) corazones o inferiores tienen una oportunidad
    para curarte para (nivel+5) corazones en su lugar.
  applies-to: ꐤ
  type: DEFENSE
  group: LEGENDARY
  applies:
  - ALL_HELMET
  levels:
    '1':
      chance: 2
      cooldown: 7
      conditions:
      - '%victim health% > 9 : %stop%'
      effects:
      - ADD_HEALTH:11 @Victim
      - MESSAGE:§6§l* DEATH GOD * @Victim
    '2':
      chance: 6
      cooldown: 10
      conditions:
      - '%victim health% > 10 : %stop%'
      effects:
      - ADD_HEALTH:12 @Victim
      - MESSAGE:§6§l* DEATH GOD * @Victim
    '3':
      chance: 11
      cooldown: 15
      conditions:
      - '%victim health% > 11 : %stop%'
      effects:
      - ADD_HEALTH:13 @Victim
      - MESSAGE:§6§l* DEATH GOD * @Victim
insanity:
  display: '%group-color%Insanity'
  description: |-
    Te balanceas el hacha como un maníaco.
    Oportunidad de multiplicar el daño contra los jugadores
    que están empuñando una espada en
    el tiempo que son golpeados.
  applies-to: ꐝ
  type: ATTACK
  group: LEGENDARY
  applies:
  - ALL_AXE
  levels:
    '1':
      chance: 17
      cooldown: 1
      conditions:
      - '%victim is holding% contains SWORD : %allow%'
      effects:
      - DOUBLE_DAMAGE
    '2':
      chance: 23
      cooldown: 1
      conditions:
      - '%victim is holding% contains SWORD : %allow%'
      effects:
      - DOUBLE_DAMAGE
    '3':
      chance: 29
      cooldown: 1
      conditions:
      - '%victim is holding% contains SWORD : %allow%'
      effects:
      - DOUBLE_DAMAGE
    '4':
      chance: 35
      cooldown: 1
      conditions:
      - '%victim is holding% contains SWORD : %allow%'
      effects:
      - DOUBLE_DAMAGE
    '5':
      chance: 41
      cooldown: 1
      conditions:
      - '%victim is holding% contains SWORD : %allow%'
      effects:
      - DOUBLE_DAMAGE
    '6':
      chance: 49
      cooldown: 1
      conditions:
      - '%victim is holding% contains SWORD : %allow%'
      effects:
      - DOUBLE_DAMAGE
    '7':
      chance: 52
      cooldown: 1
      conditions:
      - '%victim is holding% contains SWORD : %allow%'
      effects:
      - DOUBLE_DAMAGE
    '8':
      chance: 56
      cooldown: 1
      conditions:
      - '%victim is holding% contains SWORD : %allow%'
      effects:
      - DOUBLE_DAMAGE
sniper:
  display: '%group-color%Sniper'
  description: |-
    Disparos a la cabeza con proyectil
    Hacer daños hasta 3.5x.
  applies-to: ꐣ
  type: SHOOT
  group: LEGENDARY
  applies:
  - BOW
  - CROSSBOW
  levels:
    '1':
      chance: 15
      cooldown: 5
      conditions:
      - '%is headshot% = true : %allow%'
      effects:
      - INCREASE_DAMAGE:<random number>100-350</random number> @Attacker
      - MESSAGE:§6§l** HEADSHOT ** @Victim
    '2':
      chance: 20
      cooldown: 5
      conditions:
      - '%is headshot% = true : %allow%'
      effects:
      - INCREASE_DAMAGE:<random number>100-350</random number> @Attacker
      - MESSAGE:§6§l** HEADSHOT ** @Victim
    '3':
      chance: 25
      cooldown: 5
      conditions:
      - '%is headshot% = false : %stop%'
      effects:
      - INCREASE_DAMAGE:<random number>100-350</random number> @Attacker
      - MESSAGE:§6§l** HEADSHOT ** @Victim
    '4':
      chance: 30
      cooldown: 5
      conditions:
      - '%is headshot% = false : %stop%'
      effects:
      - INCREASE_DAMAGE:<random number>100-350</random number> @Attacker
      - MESSAGE:§6§l** HEADSHOT ** @Victim
    '5':
      chance: 35
      cooldown: 5
      conditions:
      - '%is headshot% = false : %stop%'
      effects:
      - INCREASE_DAMAGE:<random number>100-350</random number> @Attacker
      - MESSAGE:§6§l** HEADSHOT ** @Victim
destruction:
  display: '%group-color%Destruction'
  description: |-
    Oportunidad de daños y debuffs
    Todos los enemigos cercanos cuando están atacados.
  applies-to: ꐤ
  type: DEFENSE
  group: LEGENDARY
  applies:
  - ALL_HELMET
  levels:
    '1':
      chance: 5
      cooldown: 10
      effects:
      - DO_HARM:1 @Aoe{r=3,t=damageable}
      - CURE:INCREASE_DAMAGE @Aoe{r=3,t=damageable}
      - CURE:REGENERATION @Aoe{r=3,t=damageable}
      - CURE:SPEED @Aoe{r=3,t=damageable}
      - CURE:ABSORPTION @Aoe{r=3,t=damageable}
      - CURE:HASTE @Aoe{r=3,t=damageable}
      - MESSAGE:§e§l*** §eDesctruction §e§l*** §7(%victim name%) @Aoe{r=3,t=damageable}
    '2':
      chance: 8
      cooldown: 10
      effects:
      - DO_HARM:1 @Aoe{r=4,t=damageable}
      - CURE:INCREASE_DAMAGE @Aoe{r=4,t=damageable}
      - CURE:REGENERATION @Aoe{r=4,t=damageable}
      - CURE:SPEED @Aoe{r=4,t=damageable}
      - CURE:ABSORPTION @Aoe{r=4,t=damageable}
      - CURE:HASTE @Aoe{r=4,t=damageable}
      - MESSAGE:§e§l*** §eDesctruction §e§l*** §7(%victim name%) @Aoe{r=4,t=damageable}
    '3':
      chance: 9
      cooldown: 11
      effects:
      - DO_HARM:1 @Aoe{r=5,t=damageable}
      - CURE:INCREASE_DAMAGE @Aoe{r=5,t=damageable}
      - CURE:REGENERATION @Aoe{r=5,t=damageable}
      - CURE:SPEED @Aoe{r=5,t=damageable}
      - CURE:ABSORPTION @Aoe{r=5,t=damageable}
      - CURE:HASTE @Aoe{r=5,t=damageable}
      - MESSAGE:§e§l*** §eDesctruction §e§l*** §7(%victim name%) @Aoe{r=5,t=damageable}
    '4':
      chance: 12
      cooldown: 12
      effects:
      - DO_HARM:2 @Aoe{r=5,t=damageable}
      - CURE:INCREASE_DAMAGE @Aoe{r=5,t=damageable}
      - CURE:REGENERATION @Aoe{r=5,t=damageable}
      - CURE:SPEED @Aoe{r=5,t=damageable}
      - CURE:ABSORPTION @Aoe{r=5,t=damageable}
      - CURE:HASTE @Aoe{r=5,t=damageable}
      - MESSAGE:§e§l*** §eDesctruction §e§l*** §7(%victim name%) @Aoe{r=5,t=damageable}
    '5':
      chance: 15
      cooldown: 15
      effects:
      - DO_HARM:2 @Aoe{r=5,t=damageable}
      - CURE:INCREASE_DAMAGE @Aoe{r=5,t=damageable}
      - CURE:REGENERATION @Aoe{r=5,t=damageable}
      - CURE:SPEED @Aoe{r=5,t=damageable}
      - CURE:ABSORPTION @Aoe{r=5,t=damageable}
      - CURE:HASTE @Aoe{r=5,t=damageable}
      - MESSAGE:§e§l*** §eDesctruction §e§l*** §7(%victim name%) @Aoe{r=5,t=damageable}
extremeinsanity:
  display: '%group-color%Insanity'
  description: |-
    Giras tu espada como un maníaco extremo.
    Oportunidad de multiplicar el daño contra los jugadores
    que están empuñando una espada en
    el tiempo que son golpeados.
    Requiere Insanity VIII para aplicar.
  applies-to: ꐝ
  type: ATTACK
  settings:
    required-enchants:
    - insanity:8
    removed-enchants:
    - insanity
    removeable: false
  group: HEROIC
  applies:
  - ALL_AXE
  levels:
    '1':
      chance: 4
      cooldown: 4
      conditions:
      - '%victim is holding% contains SWORD : %allow%'
      effects:
      - DOUBLE_DAMAGE
    '2':
      chance: 8
      cooldown: 4
      conditions:
      - '%victim is holding% contains SWORD : %allow%'
      effects:
      - DOUBLE_DAMAGE
    '3':
      chance: 12
      cooldown: 5
      conditions:
      - '%victim is holding% contains SWORD : %allow%'
      effects:
      - DOUBLE_DAMAGE
    '4':
      chance: 14
      cooldown: 5
      conditions:
      - '%victim is holding% contains SWORD : %allow%'
      effects:
      - DOUBLE_DAMAGE
    '5':
      chance: 16
      cooldown: 5
      conditions:
      - '%victim is holding% contains SWORD : %allow%'
      effects:
      - DOUBLE_DAMAGE
    '6':
      chance: 19
      cooldown: 6
      conditions:
      - '%victim is holding% contains SWORD : %allow%'
      effects:
      - DOUBLE_DAMAGE
    '7':
      chance: 22
      cooldown: 7
      conditions:
      - '%victim is holding% contains SWORD : %allow%'
      effects:
      - DOUBLE_DAMAGE
    '8':
      chance: 25
      cooldown: 8
      conditions:
      - '%victim is holding% contains SWORD : %allow%'
      effects:
      - DOUBLE_DAMAGE
megaheavy:
  display: '%group-color%Mega Heavy'
  description: |-
    Oportunidad de disminuir el daño de los arcos enemigos
    por 10% más un 2% adicional
    por nivel.Requiere Heavy V para aplicar.
  applies-to: ꐤ ꐞ ꐧ ꐥ
  type: DEFENSE_PROJECTILE
  settings:
    required-enchants:
    - heavy:5
    removed-enchants:
    - heavy
    removeable: false
  group: HEROIC
  applies:
  - ALL_ARMOR
  levels:
    '1':
      chance: 4
      cooldown: 6
      conditions:
      - '%attacker is holding% contains BOW : %allow%'
      effects:
      - DECREASE_DAMAGE:12
    '2':
      chance: 7
      cooldown: 7
      conditions:
      - '%attacker is holding% contains BOW : %allow%'
      effects:
      - DECREASE_DAMAGE:14
    '3':
      chance: 8
      cooldown: 7
      conditions:
      - '%attacker is holding% contains BOW : %allow%'
      effects:
      - DECREASE_DAMAGE:16
    '4':
      chance: 10
      cooldown: 7
      conditions:
      - '%attacker is holding% contains BOW : %allow%'
      effects:
      - DECREASE_DAMAGE:18
    '5':
      chance: 12
      cooldown: 9
      conditions:
      - '%attacker is holding% contains BOW : %allow%'
      effects:
      - DECREASE_DAMAGE:20
bewitchedhex:
  display: '%group-color%Bewitched Hex'
  description: |-
    Una vez que un objetivo se ve afectado con hexadecimal,
    Una parte de todo su daño saliente es
    reducido.Cuando están atacados, reciben daño adicional.
    Requiere Hex IV para aplicar.
  applies-to: ꐝ
  type: ATTACK
  settings:
    required-enchants:
    - hex:4
    removed-enchants:
    - hex
    removeable: false
  group: HEROIC
  applies:
  - ALL_AXE
  levels:
    '1':
      chance: 6
      cooldown: 4
      effects:
      - DECREASE_DAMAGE:<random number>20-75</random number> @Victim
      - DO_HARM:<random number>5-10</random number> @Victim
    '2':
      chance: 9
      cooldown: 4
      effects:
      - DECREASE_DAMAGE:<random number>20-75</random number> @Victim
      - DO_HARM:<random number>5-10</random number> @Victim
    '3':
      chance: 13
      cooldown: 4
      effects:
      - DECREASE_DAMAGE:<random number>20-75</random number> @Victim
      - DO_HARM:<random number>5-10</random number> @Victim
    '4':
      chance: 16
      cooldown: 4
      effects:
      - DECREASE_DAMAGE:<random number>20-75</random number> @Victim
      - DO_HARM:<random number>5-10</random number> @Victim
mightycleave:
  display: '%group-color%Mighty Cleave'
  description: |-
    La oportunidad de causar hasta 8 daños en hasta 4 a 8 de 7 radio.
    Requiere Cleave VII para aplicar.
  applies-to: ꐝ
  type: ATTACK
  group: HEROIC
  settings:
    required-enchants:
    - cleave:7
    removed-enchants:
    - cleave
    removeable: false
  applies:
  - ALL_AXE
  levels:
    '1':
      chance: 4
      cooldown: 12
      effects:
      - DO_HARM:<random number>1-8</random number> @Aoe{r=1,t=damageable}
      - MESSAGE:§d§l** MIGHTY CLEAVE §7(%attacker name%)§d§l ** @Aoe{r=1,t=damageable}
    '2':
      chance: 5
      cooldown: 13
      effects:
      - DO_HARM:<random number>2-8</random number> @Aoe{r=2,t=damageable}
      - MESSAGE:§d§l** MIGHTY CLEAVE §7(%attacker name%)§d§l ** @Aoe{r=2,t=damageable}
    '3':
      chance: 7
      cooldown: 14
      effects:
      - DO_HARM:<random number>3-8</random number> @Aoe{r=3,t=damageable}
      - MESSAGE:§d§l** MIGHTY CLEAVE §7(%attacker name%)§d§l ** @Aoe{r=3,t=damageable}
    '4':
      chance: 9
      cooldown: 15
      effects:
      - DO_HARM:<random number>5-8</random number> @Aoe{r=4,t=damageable}
      - MESSAGE:§d§l** MIGHTY CLEAVE §7(%attacker name%)§d§l ** @Aoe{r=4,t=damageable}
    '5':
      chance: 9
      cooldown: 10
      effects:
      - DO_HARM:<random number>6-8</random number> @Aoe{r=5,t=damageable}
      - MESSAGE:§d§l** MIGHTY CLEAVE §7(%attacker name%)§d§l ** @Aoe{r=5,t=damageable}
mightycactus:
  display: '%group-color%Mighty Cactus'
  description: |-
    Encantamiento heroico.Oportunidad de detener el enemigo
    atacar y lesionar a tu atacante pero no
    afectar su durabilidad.Requiere Cactus II para aplicar.
  applies-to: ꐤ ꐞ ꐧ ꐥ
  type: DEFENSE
  group: HEROIC
  settings:
    required-enchants:
    - cactus:2
    removed-enchants:
    - cactus
    removeable: false
  applies:
  - ALL_ARMOR
  levels:
    '1':
      chance: 8
      cooldown: 3
      effects:
      - CANCEL_EVENT
      - DO_HARM:<random number>2-5</random number> @Attacker
      - MESSAGE:§d§l** MIGHTY CACTUS ** §7(%victim name%)
    '2':
      chance: 12
      cooldown: 3
      effects:
      - CANCEL_EVENT
      - DO_HARM:<random number>2-5</random number> @Attacker
      - MESSAGE:§d§l** MIGHTY CACTUS ** §7(%victim name%)
guidedrocketescape:
  display: '%group-color%Guided Rocket Escape'
  description: |-
    Oportunidad de volar en el aire a baja salud
    y obtenga brevemente el vuelo para (nivel X 1S).
    Requiere escape de Rocketescape III para aplicar.
  applies-to: ꐥ
  type: DEFENSE
  group: HEROIC
  settings:
    required-enchants:
    - rocketescape:3
    removed-enchants:
    - rocketescape
    removeable: false
  applies:
  - ALL_BOOTS
  levels:
    '1':
      chance: 30
      cooldown: 5
      conditions:
      - '%victim health% > 6 : %stop%'
      effects:
      - BOOST:20 @Victim
      - MESSAGE:§d§l** GUIDED ROCKET ESCAPE **@Victim
    '2':
      chance: 50
      cooldown: 5
      conditions:
      - '%victim health% > 6 : %stop%'
      effects:
      - BOOST:40 @Victim
      - MESSAGE:§d§l** GUIDED ROCKET ESCAPE **@Victim
    '3':
      chance: 70
      cooldown: 5
      conditions:
      - '%victim health% > 6 : %stop%'
      effects:
      - BOOST:60 @Victim
      - MESSAGE:§d§l** GUIDED ROCKET ESCAPE **@Victim
soulhardened:
  display: '%group-color%Soul Hardened'
  description: |-
    Hasta el 50% de posibilidades de block enemy Soul trap, la armadura recibe menos daño de durabilidad.
    Requiere Hardened III para aplicar.
  applies-to: ꐤ ꐞ ꐧ ꐥ
  type: EFFECT_STATIC
  group: HEROIC
  settings:
    required-enchants:
    - hardened:3
    removed-enchants:
    - hardened
    removeable: false
  applies:
  - ALL_ARMOR
  levels:
    '1':
      chance: 15
      cooldown: 7
      effects:
      - DISABLE_ACTIVATION:soultrap:5 @Attacker
      - ADD_DURABILITY_ARMOR:-5 @Victim
    '2':
      chance: 19
      cooldown: 7
      effects:
      - DISABLE_ACTIVATION:soultrap:5 @Attacker
      - ADD_DURABILITY_ARMOR:-5 @Victim
    '3':
      chance: 24
      cooldown: 7
      effects:
      - DISABLE_ACTIVATION:soultrap:5 @Attacker
      - ADD_DURABILITY_ARMOR:-5 @Victim
polymorphicmetaphysical:
  display: '%group-color%Polymorphic Metaphysical'
  description: |-
    Una oportunidad de ser curado de lentitud cuando se ataca.
    A nivel máximo, solo estarás
    afectado aprox.10% del tiempo.
    Requiere Metaphysical IV para aplicar.
  applies-to: ꐥ
  type: DEFENSE
  group: HEROIC
  settings:
    required-enchants:
    - metaphysical:4
    removed-enchants:
    - metaphysical
    removeable: false
  applies:
  - ALL_BOOTS
  levels:
    '1':
      chance: 30
      effects:
      - CURE:SLOW @Victim
    '2':
      chance: 60
      effects:
      - CURE:SLOW @Victim
    '3':
      chance: 75
      effects:
      - CURE:SLOW @Victim
    '4':
      chance: 90
      effects:
      - CURE:SLOW @Victim
soulbound:
  display: '%group-color%Soulbound'
  description: Una oportunidad para mantener el artículo en la muerte.
  applies-to: ꐚ ꐝ ꐜ ꐢ ꐣ ꐛ
  type: DEATH;PASSIVE_DEATH
  group: HEROIC
  applies:
  - ALL_SWORD
  - ALL_AXE
  - ALL_PICKAXE
  - ALL_SPADE
  - BOW
  - CROSSBOW
  levels:
    '1':
      chance: 4
      cooldown: 300
      effects:
      - KEEP_ON_DEATH
    '2':
      chance: 6
      cooldown: 300
      effects:
      - KEEP_ON_DEATH
    '3':
      chance: 8
      cooldown: 300
      effects:
      - KEEP_ON_DEATH
reinforcedtank:
  display: '%group-color%Reinforced Tank'
  description: |-
    Disminuye el daño del enemigo
    ejes por 6% + 2% por nivel.
    Requiere Tank IV para aplicar.
  applies-to: ꐤ ꐞ ꐧ ꐥ
  type: DEFENSE
  group: HEROIC
  settings:
    required-enchants:
    - tank:4
    removed-enchants:
    - tank
    removeable: false
  applies:
  - ALL_ARMOR
  levels:
    '1':
      chance: 5
      cooldown: 3
      conditions:
      - '%attacker is holding% contains AXE : %allow%'
      effects:
      - DECREASE_DAMAGE:8 @Victim
    '2':
      chance: 8
      cooldown: 5
      conditions:
      - '%attacker is holding% contains AXE : %allow%'
      effects:
      - DECREASE_DAMAGE:10 @Victim
    '3':
      chance: 12
      cooldown: 6
      conditions:
      - '%attacker is holding% contains AXE : %allow%'
      effects:
      - DECREASE_DAMAGE:12 @Victim
    '4':
      chance: 16
      cooldown: 8
      conditions:
      - '%attacker is holding% contains AXE : %allow%'
      effects:
      - DECREASE_DAMAGE:14 @Victim
epidemiccarrier:
  display: '%group-color%Epidemic Carrier'
  description: |-
    Cuando está cerca de la muerte, la oportunidad de convocar enredades
    y debuffs para vengarte. Carrier de peste requerido Plaguecarrier VIII para aplicar.
  applies-to: ꐞ
  type: DEFENSE
  group: HEROIC
  settings:
    required-enchants:
    - plaguecarrier:8
    removed-enchants:
    - plaguecarrier
    removeable: false
  applies:
  - ALL_LEGGINGS
  levels:
    '1':
      chance: 13
      cooldown: 15
      conditions:
      - '%victim health% > 4 : %stop%'
      effects:
      - GUARD:CREEPER:@Victim
      - GUARD:CREEPER:@Victim
      - POTION:BLINDNESS:0:40 @Attacker
    '2':
      chance: 17
      cooldown: 15
      conditions:
      - '%victim health% > 4 : %stop%'
      effects:
      - GUARD:CREEPER:@Victim
      - GUARD:CREEPER:@Victim
      - POTION:BLINDNESS:0:60 @Attacker
    '3':
      chance: 24
      cooldown: 15
      conditions:
      - '%victim health% > 4 : %stop%'
      effects:
      - GUARD:CREEPER:@Victim
      - GUARD:CREEPER:@Victim
      - GUARD:CREEPER:@Victim
      - POTION:BLINDNESS:0:100 @Attacker
    '4':
      chance: 30
      cooldown: 15
      conditions:
      - '%victim health% > 4 : %stop%'
      effects:
      - GUARD:CREEPER:@Victim
      - GUARD:CREEPER:@Victim
      - GUARD:CREEPER:@Victim
      - POTION:BLINDNESS:1:40 @Attacker
    '5':
      chance: 38
      cooldown: 15
      conditions:
      - '%victim health% > 4 : %stop%'
      effects:
      - GUARD:CREEPER:@Victim
      - GUARD:CREEPER:@Victim
      - GUARD:CREEPER:@Victim
      - POTION:BLINDNESS:1:80 @Attacker
    '6':
      chance: 46
      cooldown: 15
      conditions:
      - '%victim health% > 4 : %stop%'
      effects:
      - GUARD:CREEPER:@Victim
      - GUARD:CREEPER:@Victim
      - GUARD:CREEPER:@Victim
      - GUARD:CREEPER:@Victim
      - POTION:BLINDNESS:1:120 @Attacker
    '7':
      chance: 55
      cooldown: 15
      conditions:
      - '%victim health% > 4 : %stop%'
      effects:
      - GUARD:CREEPER:@Victim
      - GUARD:CREEPER:@Victim
      - GUARD:CREEPER:@Victim
      - GUARD:CREEPER:@Victim
      - POTION:BLINDNESS:2:60 @Attacker
    '8':
      chance: 69
      cooldown: 15
      conditions:
      - '%victim health% > 4 : %stop%'
      effects:
      - GUARD:CREEPER:@Victim
      - GUARD:CREEPER:@Victim
      - GUARD:CREEPER:@Victim
      - GUARD:CREEPER:@Victim
      - POTION:BLINDNESS:2:100 @Attacker
godlyoverload:
  display: '%group-color%Godly Overload'
  description: |-
    Encantamiento heroico.Un muy grande
    Aumento permanente en los corazones.Requerimiento
    Overload III enciende en el elemento para aplicar.
  applies-to: ꐤ ꐞ ꐧ ꐥ
  type: EFFECT_STATIC
  group: HEROIC
  settings:
    required-enchants:
    - overload:3
    removed-enchants:
    - overload
    removeable: false
  applies:
  - ALL_ARMOR
  levels:
    '1':
      effects:
      - POTION:HEALTH_BOOST:2
    '2':
      effects:
      - POTION:HEALTH_BOOST:3
    '3':
      effects:
      - POTION:HEALTH_BOOST:4
reflectiveblock:
  display: '%group-color%Reflective Block'
  description: |-
    Encantamiento heroico.
    Una oportunidad de negar en gran medida o completamente
    daño entrante mientras bloquea, y
    Para reflejar un ataque entrante de regreso
    en el atacante si estás bloqueando
    O no. Requiere el Block III para aplicar.
  applies-to: ꐚ
  type: DEFENSE
  group: HEROIC
  settings:
    required-enchants:
    - block:3
    removed-enchants:
    - block
    removeable: false
  applies:
  - ALL_SWORD
  levels:
    '1':
      chance: 16
      cooldown: 7
      effects:
      - CANCEL_EVENT
      - DO_HARM:%damage% @Attacker
    '2':
      chance: 22
      cooldown: 7
      effects:
      - CANCEL_EVENT
      - DO_HARM:%damage% @Attacker
    '3':
      chance: 30
      cooldown: 7
      effects:
      - CANCEL_EVENT
      - DO_HARM:%damage% @Attacker
masterinquisitive:
  display: '%group-color%Master Inquisitive'
  description: |-
    Encantamiento heroico.Oportunidad de masivamente
    Aumenta las caídas de EXP de los monstruos.
    Requiere Inquisitive IV Enchant
    en el artículo para aplicar.
  applies-to: ꐚ
  type: KILL_MOB
  group: HEROIC
  settings:
    required-enchants:
    - inquisitive:4
    removed-enchants:
    - inquisitive
    removeable: false
  applies:
  - ALL_SWORD
  levels:
    '1':
      chance: 60
      cooldown: 2
      effects:
      - EXP:<math>(%exp% * (1.0 + 0.25 * %level%))*2.0</math> @Victim
    '2':
      chance: 70
      cooldown: 2
      effects:
      - EXP:<math>(%exp% * (1.0 + 0.25 * %level%))*2.0</math> @Victim
    '3':
      chance: 80
      cooldown: 2
      effects:
      - EXP:<math>(%exp% * (1.0 + 0.25 * %level%))*2.0</math> @Victim
    '4':
      chance: 90
      cooldown: 2
      effects:
      - EXP:<math>(%exp% * (1.0 + 0.25 * %level%))*2.0</math> @Victim
planetarydeathbringer:
  display: '%group-color%Planetary Deathbringer'
  description: |-
    Encantamiento heroico.Un aumento
    oportunidad de causar daños 1.5x.Requerimiento
    Deathbringer III enciende en el elemento para aplicar.
  applies-to: ꐤ ꐞ ꐧ ꐥ
  type: ATTACK
  group: HEROIC
  settings:
    required-enchants:
    - deathbringer:3
    removed-enchants:
    - deathbringer
    removeable: false
  applies:
  - ALL_ARMOR
  levels:
    '1':
      chance: 20
      cooldown: 20
      effects:
      - INCREASE_DAMAGE:50 @Attacker
    '2':
      chance: 26
      cooldown: 20
      effects:
      - INCREASE_DAMAGE:50 @Attacker
    '3':
      chance: 32
      cooldown: 20
      effects:
      - INCREASE_DAMAGE:50 @Attacker
divineenlighted:
  display: '%group-color%Divine Enlighted'
  description: |-
    Encantamiento heroico.Alta posibilidad de
    curando mucho HP mientras recibe daño.Requerimiento
    Enlighted III enciende en el elemento para aplicar.
  applies-to: ꐤ ꐞ ꐧ ꐥ
  type: DEFENSE
  group: HEROIC
  settings:
    required-enchants:
    - enlighted:3
    removed-enchants:
    - enlighted
    removeable: false
  applies:
  - ALL_ARMOR
  levels:
    '1':
      chance: 5
      cooldown: 5
      effects:
      - ADD_HEALTH:<random number>1-4</random number> @Victim
    '2':
      chance: 10
      cooldown: 7
      effects:
      - ADD_HEALTH:<random number>1-4</random number> @Victim
    '3':
      chance: 15
      cooldown: 9
      effects:
      - ADD_HEALTH:<random number>1-4</random number> @Victim
lethalsniper:
  display: '%group-color%Lethal Sniper'
  description: |-
    Encantamiento heroico.Aumentó
    oportunidad de disparo en la cabeza y daño multiplicado
    hasta 4.5x.Requiere Sniper V
    Encantado en el artículo para aplicar.
  applies-to: ꐣ
  type: SHOOT
  group: HEROIC
  settings:
    required-enchants:
    - sniper:5
    removed-enchants:
    - sniper
    removeable: false
  applies:
  - BOW
  - CROSSBOW
  levels:
    '1':
      chance: 22
      cooldown: 4
      conditions:
      - '%is headshot% = true : %allow%'
      effects:
      - INCREASE_DAMAGE:<random number>100-450</random number> @Attacker
      - MESSAGE:§d§l** LETHAL HEADSHOT ** @Victim
    '2':
      chance: 27
      cooldown: 4
      conditions:
      - '%is headshot% = true : %allow%'
      effects:
      - INCREASE_DAMAGE:<random number>100-450</random number> @Attacker
      - MESSAGE:§d§l** LETHAL HEADSHOT ** @Victim
    '3':
      chance: 33
      cooldown: 4
      conditions:
      - '%is headshot% = true : %allow%'
      effects:
      - INCREASE_DAMAGE:<random number>100-450</random number> @Attacker
      - MESSAGE:§d§l** LETHAL HEADSHOT ** @Victim
    '4':
      chance: 39
      cooldown: 4
      conditions:
      - '%is headshot% = true : %allow%'
      effects:
      - INCREASE_DAMAGE:<random number>100-450</random number> @Attacker
      - MESSAGE:§d§l** LETHAL HEADSHOT ** @Victim
    '5':
      chance: 43
      cooldown: 4
      conditions:
      - '%is headshot% = true : %allow%'
      effects:
      - INCREASE_DAMAGE:<random number>100-450</random number> @Attacker
      - MESSAGE:§d§l** LETHAL HEADSHOT ** @Victim
atomicdetonate:
  display: '%group-color%Atomic Detonate'
  description: |-
    Encantamiento heroico. Citación a un
    Explosión de 7x7 alrededor de cualquier bloque
    romper.Requiere Detonate XI en el artículo para aplicar.
  applies-to: ꐝ ꐜ ꐢ
  type: MINING
  group: HEROIC
  settings:
    required-enchants:
    - detonate:9
    removed-enchants:
    - detonate
    removeable: false
  applies:
  - ALL_PICKAXE
  - ALL_SPADE
  - ALL_AXE
  levels:
    '1':
      chance: 13
      effects:
      - BREAK_BLOCK @Trench{r=7}
    '2':
      chance: 26
      effects:
      - BREAK_BLOCK @Trench{r=7}
    '3':
      chance: 36
      effects:
      - BREAK_BLOCK @Trench{r=7}
    '4':
      chance: 49
      effects:
      - BREAK_BLOCK @Trench{r=7}
    '5':
      chance: 59
      effects:
      - BREAK_BLOCK @Trench{r=7}
    '6':
      chance: 72
      effects:
      - BREAK_BLOCK @Trench{r=7}
    '7':
      chance: 85
      effects:
      - BREAK_BLOCK @Trench{r=7}
    '8':
      chance: 90
      effects:
      - BREAK_BLOCK @Trench{r=7}
    '9':
      effects:
      - BREAK_BLOCK @Trench{r=7}
titantrap:
  display: '%group-color%Titan Trap'
  description: |-
    Encantamiento heroico.Una oportunidad para
    Dar un mejor pulido duradero
    efecto de lentitud.Requiere Trap III para aplicar.
  applies-to: ꐚ
  type: ATTACK
  group: HEROIC
  settings:
    required-enchants:
    - trap:3
    removed-enchants:
    - trap
    removeable: false
  applies:
  - ALL_SWORD
  levels:
    '1':
      chance: 16
      cooldown: 40
      effects:
      - POTION:SLOW:40:60 @Victim
      - MESSAGE:§c§l** TITAN TRAP [§73s§c§l**
    '2':
      chance: 21
      cooldown: 40
      effects:
      - POTION:SLOW:40:80 @Victim
      - MESSAGE:§c§l** TITAN TRAP [§74s§c§l**
    '3':
      chance: 27
      cooldown: 40
      effects:
      - POTION:SLOW:40:120 @Victim
      - MESSAGE:§c§l** TITAN TRAP [§76s§c§l**
bidirectionalteleportation:
  display: '%group-color%Bidirectional Teleportation'
  description: Encantamiento heroico.Oportunidad de lidiar a un enemigo hacia ti.
  applies-to: ꐣ
  type: SHOOT
  group: HEROIC
  applies:
  - BOW
  - CROSSBOW
  levels:
    '1':
      chance: 12
      cooldown: 4
      effects:
      - PULL_CLOSER:2.0 @Victim
    '2':
      chance: 23
      cooldown: 5
      effects:
      - PULL_CLOSER:2.0 @Victim
    '3':
      chance: 32
      cooldown: 5
      effects:
      - PULL_CLOSER:3.0 @Victim
    '4':
      chance: 44
      cooldown: 5
      effects:
      - PULL_CLOSER:3.0 @Victim
masterblacksmith:
  display: '%group-color%Master Blacksmith'
  description: |-
    Oportunidad de sanar tu más dañado
    trozo de armadura por 2-3 durabilidad siempre que
    Golpeas a un jugador, pero cuando procesa tu
    El ataque abordará entre 75% -100% de daño.
    Requiere Blacksmith V Enchantment en el elemento para aplicar.
  applies-to: ꐝ
  type: ATTACK
  group: HEROIC
  applies:
  - ALL_AXE
  settings:
    required-enchants:
    - blacksmith:5
    removed-enchants:
    - blacksmith
    removeable: false
  levels:
    '1':
      chance: 12
      cooldown: 3
      effects:
      - ADD_DURABILITY_ARMOR:-2
      - DECREASE_DAMAGE:<random number>1-25</random number>
      - MESSAGE:§d§l** MASTER BLACKSMITH ** @Attacker
    '2':
      chance: 16
      cooldown: 3
      effects:
      - ADD_DURABILITY_ARMOR:-2
      - DECREASE_DAMAGE:<random number>1-25</random number>
      - MESSAGE:§d§l** MASTER BLACKSMITH ** @Attacker
    '3':
      chance: 22
      cooldown: 3
      effects:
      - ADD_DURABILITY_ARMOR:-2
      - DECREASE_DAMAGE:<random number>1-25</random number>
      - MESSAGE:§d§l** MASTER BLACKSMITH ** @Attacker
    '4':
      chance: 29
      cooldown: 3
      effects:
      - ADD_DURABILITY_ARMOR:-3
      - DECREASE_DAMAGE:<random number>1-25</random number>
      - MESSAGE:§d§l** MASTER BLACKSMITH ** @Attacker
    '5':
      chance: 35
      cooldown: 3
      effects:
      - ADD_DURABILITY_ARMOR:-3
      - DECREASE_DAMAGE:<random number>1-25</random number>
      - MESSAGE:§d§l** MASTER BLACKSMITH ** @Attacker
vengefuldiminish:
  display: '%group-color%Vengeful Diminish'
  description: |-
    Asegura que el próximo strike en su contra
    Solo trata el 50% del daño infligido y
    cualquier extra arriba que se devuelva
    al atacante.Requiere Diminish VI
    Encantado en el artículo para aplicar.
  applies-to: ꐧ
  type: DEFENSE
  group: HEROIC
  applies:
  - ALL_CHESTPLATE
  settings:
    required-enchants:
    - diminish:6
    removed-enchants:
    - diminish
    removeable: false
  levels:
    '1':
      chance: 6
      cooldown: 14
      effects:
      - HALF_DAMAGE
      - DO_HARM:%damage% @Attacker
    '2':
      chance: 12
      cooldown: 14
      effects:
      - HALF_DAMAGE
      - DO_HARM:%damage% @Attacker
    '3':
      chance: 17
      cooldown: 14
      effects:
      - HALF_DAMAGE
      - DO_HARM:%damage% @Attacker
    '4':
      chance: 23
      cooldown: 14
      effects:
      - HALF_DAMAGE
      - DO_HARM:%damage% @Attacker
    '5':
      chance: 28
      cooldown: 14
      effects:
      - HALF_DAMAGE
      - DO_HARM:%damage% @Attacker
    '6':
      chance: 33
      cooldown: 14
      effects:
      - HALF_DAMAGE
      - DO_HARM:%damage% @Attacker
alienimplants:
  display: '%group-color%Alien Implants'
  description: |-
    Sanar 2x el HP de
    implantes normales, y
    A nivel máximo, toda la pérdida de hambre es
    desactivado.Requiere Implants III.
  applies-to: ꐤ
  type: REPEATING
  time: 5
  group: HEROIC
  applies:
  - ALL_HELMET
  settings:
    required-enchants:
    - implants:3
    removed-enchants:
    - implants
    removeable: false
  levels:
    '1':
      chance: 20
      cooldown: 5
      effects:
      - ADD_HEALTH:2
      - ADD_FOOD:2
    '2':
      chance: 30
      cooldown: 5
      effects:
      - ADD_HEALTH:2
      - ADD_FOOD:2
    '3':
      chance: 40
      cooldown: 5
      effects:
      - ADD_HEALTH:2
      - ADD_FOOD:10
etherealdodge:
  display: '%group-color%Ethereal Dodge'
  description: |-
    Aumento de la tasa de proceso sobre el esquivo normal,
    con una pequeña oportunidad de ganar velocidad V
    por unos segundos en exitosos
    Requiere Dodge V.
  applies-to: ꐤ ꐞ ꐧ ꐥ
  type: DEFENSE
  group: HEROIC
  applies:
  - ALL_ARMOR
  settings:
    required-enchants:
    - dodge:5
    removed-enchants:
    - dodge
    removeable: false
  levels:
    '1':
      chance: 30
      cooldown: 45
      conditions:
      - '%victim is sneaking% = true : %chance%+5'
      effects:
      - CANCEL_EVENT
      - MESSAGE:§d§l** ETHEREAL DODGE* * @Victim
      - POTION:SPEED:4:80 @Victim
paladinarmored:
  display: '%group-color%Paladin Armored'
  description: |-
    Niega 10 + 5 por nivel de daño enemigo de la espada. Una oportunidad
    ser bendecido cada vez que
    son golpeados por una espada enemiga.
    Requiere Armored IV.
  applies-to: ꐤ ꐞ ꐧ ꐥ
  type: DEFENSE
  group: HEROIC
  applies:
  - ALL_ARMOR
  settings:
    required-enchants:
    - armored:4
    removed-enchants:
    - armored
    removeable: false
  levels:
    '1':
      chance: 6
      cooldown: 5
      conditions:
      - '%attacker is holding% contains SWORD : %allow%'
      effects:
      - NEGATE_DAMAGE:15 @Attacker
    '2':
      chance: 9
      cooldown: 6
      conditions:
      - '%attacker is holding% contains SWORD : %allow%'
      effects:
      - NEGATE_DAMAGE:20 @Attacker
    '3':
      chance: 11
      cooldown: 8
      conditions:
      - '%attacker is holding% contains SWORD : %allow%'
      effects:
      - NEGATE_DAMAGE:25 @Attacker
    '4':
      chance: 14
      cooldown: 8
      conditions:
      - '%attacker is holding% contains SWORD : %allow%'
      effects:
      - NEGATE_DAMAGE:30 @Attacker
demoniclifesteal:
  display: '%group-color%Demonic Lifesteal'
  description: |-
    Cura mucho más HP en gran medida
    mayor tasa en comparación con lo normal
    LifeSeal.Requiere LifeSteal V.
  applies-to: ꐚ
  type: ATTACK
  group: HEROIC
  applies:
  - ALL_SWORD
  settings:
    required-enchants:
    - lifesteal:5
    removed-enchants:
    - lifesteal
    removeable: false
  levels:
    '1':
      chance: 5.9
      cooldown: 25
      effects:
      - ADD_HEALTH:<random number>2-3</random number> @Attacker
      - MESSAGE:§d§l** DEMONIC LIFESTEAL ** §7(§c- %random%HP§7) @Attacker
    '2':
      chance: 9.3
      cooldown: 25
      effects:
      - ADD_HEALTH:<random number>2-3</random number> @Attacker
      - MESSAGE:§d§l** DEMONIC LIFESTEAL ** §7(§c- %random%HP§7) @Attacker
    '3':
      chance: 11.4
      cooldown: 25
      effects:
      - ADD_HEALTH:<random number>3-4</random number> @Attacker
      - MESSAGE:§d§l** DEMONIC LIFESTEAL ** §7(§c- %random%HP§7) @Attacker
    '4':
      chance: 13.9
      cooldown: 25
      effects:
      - ADD_HEALTH:<random number>3-4</random number> @Attacker
      - MESSAGE:§d§l** DEMONIC LIFESTEAL ** §7(§c- %random%HP§7) @Attacker
    '5':
      chance: 15
      cooldown: 25
      effects:
      - ADD_HEALTH:<random number>5-6</random number> @Attacker
      - MESSAGE:§d§l** DEMONIC LIFESTEAL ** §7(§c- %random%HP§7) @Attacker
deepbleed:
  display: '%group-color%Deep Bleed'
  description: |-
    Encantamiento heroico.Una oportunidad
    afectar en los enemigos con aumento
    lentitud e inflige más daño.
    Requiere Bleed VI.
  applies-to: ꐝ
  type: ATTACK
  group: HEROIC
  settings:
    required-enchants:
    - bleed:6
    removed-enchants:
    - bleed
    removeable: false
  applies:
  - ALL_AXE
  levels:
    '1':
      chance: 10
      cooldown: 4
      effects:
      - POTION:SLOW:2:100 @Victim
      - DO_HARM:<random number>2-6</random number> @Victim
      - MESSAGE:§d§l** Hemorragia! ** @Victim
      - WAIT:20
      - DO_HARM:<random number>1-4</random number> @Victim
    '2':
      chance: 15
      cooldown: 4
      effects:
      - POTION:SLOW:2:100 @Victim
      - DO_HARM:<random number>2-6</random number> @Victim
      - MESSAGE:§d§l** Hemorragia! ** @Victim
      - WAIT:20
      - DO_HARM:<random number>1-4</random number> @Victim
    '3':
      chance: 23
      cooldown: 4
      effects:
      - POTION:SLOW:3:100 @Victim
      - DO_HARM:<random number>2-6</random number> @Victim
      - MESSAGE:§d§l** Hemorragia! ** @Victim
      - WAIT:20
      - DO_HARM:<random number>1-4</random number> @Victim
    '4':
      chance: 30
      cooldown: 4
      effects:
      - POTION:SLOW:3:100 @Victim
      - DO_HARM:<random number>2-6</random number> @Victim
      - MESSAGE:§d§l** Hemorragia! ** @Victim
      - WAIT:20
      - DO_HARM:<random number>1-4</random number> @Victim
    '5':
      chance: 44
      cooldown: 4
      effects:
      - POTION:SLOW:3:100 @Victim
      - DO_HARM:<random number>2-6</random number> @Victim
      - MESSAGE:§d§l** Hemorragia! ** @Victim
      - WAIT:20
      - DO_HARM:<random number>1-4</random number> @Victim
    '6':
      chance: 57
      cooldown: 4
      effects:
      - POTION:SLOW:4:100 @Victim
      - DO_HARM:<random number>2-6</random number> @Victim
      - MESSAGE:§d§l** Hemorragia! ** @Victim
      - WAIT:20
      - DO_HARM:<random number>1-3</random number> @Victim
      - WAIT:20
      - DO_HARM:<random number>1-4</random number> @Victim
shadowassassin:
  display: '%group-color%Shadow Assassin'
  description: |-
    Encantamiento heroico.El
    más cerca estás con tu enemigo,
    Cuanto más daño le otorgue
    (hasta 1.875x).Sin embargo, si tu
    están a más de 2 cuadras de distancia,
    causará menos daño de lo normal.
    Requiere Assassin V.
  applies-to: ꐚ
  type: ATTACK
  group: HEROIC
  settings:
    required-enchants:
    - assassin:5
    removed-enchants:
    - assassin
    removeable: false
  applies:
  - ALL_SWORD
  levels:
    '1':
      chance: 7
      cooldown: 3
      effects:
      - MESSAGE:&c(Removed) DISTANCE_DAMAGE:5:1 @Attacker
    '2':
      chance: 12
      cooldown: 3
      effects:
      - MESSAGE:&c(Removed) DISTANCE_DAMAGE:5:1 @Attacker
    '3':
      chance: 19
      cooldown: 3
      effects:
      - MESSAGE:&c(Removed) DISTANCE_DAMAGE:5:1 @Attacker
    '4':
      chance: 24
      cooldown: 3
      effects:
      - MESSAGE:&c(Removed) DISTANCE_DAMAGE:5:1 @Attacker
    '5':
      chance: 29
      cooldown: 3
      effects:
      - MESSAGE:&c(Removed) DISTANCE_DAMAGE:5:1 @Attacker
rogue:
  display: '%group-color%Rogue'
  description: Alma activa encantadora.Oportunidad de causar hasta 2.0x de daño.
  applies-to: ꐝ
  type: ATTACK
  group: SOUL
  applies:
  - ALL_AXE
  levels:
    '1':
      chance: 13
      cooldown: 3
      souls: 100
      effects:
      - INCREASE_DAMAGE:<random number>25-100</random number> @Attacker
    '2':
      chance: 16
      cooldown: 3
      souls: 100
      effects:
      - INCREASE_DAMAGE:<random number>25-100</random number> @Attacker
    '3':
      chance: 19
      cooldown: 3
      souls: 100
      effects:
      - INCREASE_DAMAGE:<random number>25-100</random number> @Attacker
sabotage:
  display: '%group-color%Sabotage'
  description: |-
    Un encanto activo del alma que da la oportunidad de block
    Los jugadores enemigos escapan y guiaron el escape de cohetes de la activación.
  applies-to: ꐚ
  type: ATTACK
  group: SOUL
  applies:
  - ALL_SWORD
  levels:
    '1':
      chance: 12
      souls: 4
      effects:
      - DISABLE_ACTIVATION:rocketescape:3 @Victim
      - DISABLE_ACTIVATION:guidedrocketescape:3 @Victim
    '2':
      chance: 16
      souls: 4
      effects:
      - DISABLE_ACTIVATION:rocketescape:3 @Victim
      - DISABLE_ACTIVATION:guidedrocketescape:3 @Victim
    '3':
      chance: 20
      souls: 4
      effects:
      - DISABLE_ACTIVATION:rocketescape:3 @Victim
      - DISABLE_ACTIVATION:guidedrocketescape:3 @Victim
    '4':
      chance: 24
      souls: 4
      effects:
      - DISABLE_ACTIVATION:rocketescape:3 @Victim
      - DISABLE_ACTIVATION:guidedrocketescape:3 @Victim
    '5':
      chance: 28
      souls: 4
      effects:
      - DISABLE_ACTIVATION:rocketescape:3 @Victim
      - DISABLE_ACTIVATION:guidedrocketescape:3 @Victim
natureswrath:
  display: '%group-color%Natures Wrath'
  description: |-
    Congelar temporalmente a todos los enemigos en
    un área masiva a tu alrededor, empujando
    ellos de regreso y tratando de naturaleza masiva
    daño.75 almas por uso.
  applies-to: ꐤ ꐞ ꐧ ꐥ
  type: DEFENSE
  group: SOUL
  applies:
  - ALL_ARMOR
  levels:
    '1':
      chance: 5
      cooldown: 30
      souls: 75
      effects:
      - POTION:SLOW:10:60 @Attacker
      - LIGHTNING @Attacker
      - MESSAGE:§2§l** NATURES WRATH ** @Attacker
      - WAIT:20
      - LIGHTNING @Attacker
      - MESSAGE:§2§l** NATURES WRATH ** @Attacker
    '2':
      chance: 9
      cooldown: 30
      souls: 75
      effects:
      - POTION:SLOW:10:60 @Attacker
      - LIGHTNING @Attacker
      - MESSAGE:§2§l** NATURES WRATH ** @Attacker
      - WAIT:20
      - LIGHTNING @Attacker
      - MESSAGE:§2§l** NATURES WRATH ** @Attacker
    '3':
      chance: 15
      cooldown: 30
      souls: 75
      effects:
      - POTION:SLOW:10:60 @Attacker
      - LIGHTNING @Attacker
      - MESSAGE:§2§l** NATURES WRATH ** @Attacker
      - WAIT:20
      - LIGHTNING @Attacker
      - MESSAGE:§2§l** NATURES WRATH ** @Attacker
    '4':
      chance: 23
      cooldown: 30
      souls: 75
      effects:
      - POTION:SLOW:10:60 @Attacker
      - LIGHTNING @Attacker
      - MESSAGE:§2§l** NATURES WRATH ** @Attacker
      - WAIT:20
      - LIGHTNING @Attacker
      - MESSAGE:§2§l** NATURES WRATH ** @Attacker
phoenix:
  display: '%group-color%Phoenix'
  description: |-
    Un ataque que normalmente
    matarte en su lugar te curará para
    HP completo.Solo se puede activar una vez cada
    un par de minutos.500 almas por uso.
  applies-to: ꐤ ꐞ ꐧ ꐥ
  type: DEFENSE
  group: SOUL
  applies:
  - ALL_ARMOR
  levels:
    '1':
      chance: 6
      cooldown: 120
      souls: 500
      conditions:
      - '%victim health% > 3 : %stop%'
      effects:
      - ADD_HEALTH:40 @Victim
      - MESSAGE:§c§l** PHOENIX ** @Victim
      - PLAY_SOUND:ITEM_BREAK:4 @Victim
    '2':
      chance: 9
      cooldown: 120
      souls: 500
      conditions:
      - '%victim health% > 3 : %stop%'
      effects:
      - ADD_HEALTH:40 @Victim
      - MESSAGE:§c§l** PHOENIX ** @Victim
      - PLAY_SOUND:ITEM_BREAK:4 @Victim
    '3':
      chance: 15
      cooldown: 120
      souls: 500
      conditions:
      - '%victim health% > 3 : %stop%'
      effects:
      - ADD_HEALTH:40 @Victim
      - MESSAGE:§c§l** PHOENIX ** @Victim
      - PLAY_SOUND:ITEM_BREAK:4 @Victim
teleblock:
  display: '%group-color%Teleblock'
  description: |-
    Alma activa encantadora.Tu arco está encantado con Enderpearl Bloking Magic.
    Una posibilidad de que los jugadores dañados no puedan usar Enderpearls por hasta 20 segundos
    y perderá hasta 15 Enderpearls de su inventario.
  applies-to: ꐣ
  type: SHOOT
  group: SOUL
  applies:
  - BOW
  - CROSSBOW
  levels:
    '1':
      chance: 24
      cooldown: 3
      souls: 40
      effects:
      - CANCEL_USE:ENDER_PEARL:150 @Victim
      - TAKE_AWAY:ENDER_PEARL:3 @Victim
      - MESSAGE:§c§l** TELEBLOCK ** @Victim
    '2':
      chance: 32
      cooldown: 3
      souls: 40
      effects:
      - CANCEL_USE:ENDER_PEARL:150 @Victim
      - TAKE_AWAY:ENDER_PEARL:3 @Victim
      - MESSAGE:§c§l** TELEBLOCK ** @Victim
    '3':
      chance: 40
      cooldown: 3
      souls: 40
      effects:
      - CANCEL_USE:ENDER_PEARL:150 @Victim
      - TAKE_AWAY:ENDER_PEARL:3 @Victim
      - MESSAGE:§c§l** TELEBLOCK ** @Victim
    '4':
      chance: 48
      cooldown: 3
      souls: 40
      effects:
      - CANCEL_USE:ENDER_PEARL:150 @Victim
      - TAKE_AWAY:ENDERPEARL:3 @Victim
      - MESSAGE:§c§l** TELEBLOCK ** @Victim
    '5':
      chance: 60
      cooldown: 3
      souls: 40
      effects:
      - CANCEL_USE:ENDER_PEARL:150 @Victim
      - TAKE_AWAY:ENDERPEARL:3 @Victim
      - MESSAGE:§c§l** TELEBLOCK ** @Victim
soultrap:
  display: '%group-color%Soul Trap'
  description: |-
    Alma activa encantadora.Tu arma
    está imbuido de sellado de magia, y
    tiene la oportunidad de deshabilitar/negar todo
    encantamientos de alma de tus enemigos
    en Hit para (nivel X 4) segundos.
    2 almas por segundo.
  applies-to: ꐚ ꐝ
  type: ATTACK
  group: SOUL
  applies:
  - ALL_AXE
  - ALL_SWORD
  levels:
    '1':
      chance: 19
      souls: 2
      effects:
      - DISABLE_ACTIVATION:divineimmolation:4
      - DISABLE_ACTIVATION:naturewrath:4
      - DISABLE_ACTIVATION:phoenix:4
      - DISABLE_ACTIVATION:immortal:4
      - MESSAGE:§c§l** SOUL TRAP ** @Victim
    '2':
      chance: 27
      souls: 2
      effects:
      - DISABLE_ACTIVATION:divineimmolation:8
      - DISABLE_ACTIVATION:naturewrath:8
      - DISABLE_ACTIVATION:phoenix:8
      - DISABLE_ACTIVATION:immortal:8
      - MESSAGE:§c§l** SOUL TRAP ** @Victim
    '3':
      chance: 32
      souls: 2
      effects:
      - DISABLE_ACTIVATION:divineimmolation:12
      - DISABLE_ACTIVATION:naturewrath:12
      - DISABLE_ACTIVATION:phoenix:12
      - DISABLE_ACTIVATION:immortal:12
      - MESSAGE:§c§l** SOUL TRAP ** @Victim
immortal:
  display: '%group-color%Immortal'
  description: |-
    Alma pasiva encantadora.
    Oportunidad de evitar que tu armadura tome
    Daño de durabilidad, a cambio de almas.
    5 almas por uso.
  applies-to: ꐤ ꐞ ꐧ ꐥ
  type: DEFENSE
  group: SOUL
  applies:
  - ALL_ARMOR
  levels:
    '1':
      chance: 12
      cooldown: 40
      souls: 5
      effects:
      - ADD_DURABILITY_ARMOR:-10 @Victim
    '2':
      chance: 18
      cooldown: 40
      souls: 5
      effects:
      - ADD_DURABILITY_ARMOR:-10 @Victim
    '3':
      chance: 25
      cooldown: 40
      souls: 5
      effects:
      - ADD_DURABILITY_ARMOR:-10 @Victim
    '4':
      chance: 31
      cooldown: 40
      souls: 5
      effects:
      - ADD_DURABILITY_ARMOR:-10 @Victim
divineimmolation:
  display: '%group-color%Divine Immolation'
  description: |-
    Alma activa encantadora.Oportunidad para tu espada
    estar imbuido de fuego divino, girando
    Todos tus ataques físicos en el área de
    Hechizos de efecto y encender fuego divino
    Sobre todos los enemigos cercanos.
    75 almas por uso.
  applies-to: ꐚ
  type: ATTACK
  group: SOUL
  applies:
  - ALL_SWORD
  levels:
    '1':
      chance: 7
      cooldown: 15
      souls: 75
      effects:
      - PARTICLE:BURN:20:2@Aoe{r=5,t=damageable}
      - BURN:2 @Aoe{r=5,t=damageable}
      - DO_HARM:2 @Aoe{r=5,t=damageable}
      - MESSAGE:§c§l** DIVINE IMMOLATION ** @Aoe{r=5,t=damageable}
      - WAIT:20
      - BURN:2 @Aoe{r=5,t=damageable}
      - DO_HARM:2 @Aoe{r=5,t=damageable}
      - MESSAGE:§c§l** DIVINE IMMOLATION ** @Aoe{r=5,t=damageable}
      - WAIT:20
      - BURN:2 @Aoe{r=5,t=damageable}
      - DO_HARM:2 @Aoe{r=5,t=damageable}
      - MESSAGE:§c§l** DIVINE IMMOLATION ** @Aoe{r=5,t=damageable}
    '2':
      chance: 13
      cooldown: 15
      souls: 75
      effects:
      - PARTICLE:BURN:20:2@Aoe{r=5,t=damageable}
      - BURN:2 @Aoe{r=5,t=damageable}
      - DO_HARM:2 @Aoe{r=5,t=damageable}
      - MESSAGE:§c§l** DIVINE IMMOLATION ** @Aoe{r=5,t=damageable}
      - WAIT:20
      - BURN:2 @Aoe{r=5,t=damageable}
      - DO_HARM:2 @Aoe{r=5,t=damageable}
      - MESSAGE:§c§l** DIVINE IMMOLATION ** @Aoe{r=5,t=damageable}
      - WAIT:20
      - BURN:2 @Aoe{r=5,t=damageable}
      - DO_HARM:2 @Aoe{r=5,t=damageable}
      - MESSAGE:§c§l** DIVINE IMMOLATION ** @Aoe{r=5,t=damageable}
    '3':
      chance: 23
      cooldown: 15
      souls: 75
      effects:
      - PARTICLE:BURN:20:2@Aoe{r=5,t=damageable}
      - BURN:2 @Aoe{r=5,t=damageable}
      - DO_HARM:2 @Aoe{r=5,t=damageable}
      - MESSAGE:§c§l** DIVINE IMMOLATION ** @Aoe{r=5,t=damageable}
      - WAIT:20
      - BURN:2 @Aoe{r=5,t=damageable}
      - DO_HARM:2 @Aoe{r=5,t=damageable}
      - MESSAGE:§c§l** DIVINE IMMOLATION ** @Aoe{r=5,t=damageable}
      - WAIT:20
      - BURN:2 @Aoe{r=5,t=damageable}
      - DO_HARM:2 @Aoe{r=5,t=damageable}
      - MESSAGE:§c§l** DIVINE IMMOLATION ** @Aoe{r=5,t=damageable}
    '4':
      chance: 26
      cooldown: 15
      souls: 75
      effects:
      - PARTICLE:BURN:20:2@Aoe{r=5,t=damageable}
      - BURN:2 @Aoe{r=5,t=damageable}
      - DO_HARM:2 @Aoe{r=5,t=damageable}
      - MESSAGE:§c§l** DIVINE IMMOLATION ** @Aoe{r=5,t=damageable}
      - WAIT:20
      - BURN:2 @Aoe{r=5,t=damageable}
      - DO_HARM:2 @Aoe{r=5,t=damageable}
      - MESSAGE:§c§l** DIVINE IMMOLATION ** @Aoe{r=5,t=damageable}
      - WAIT:20
      - BURN:2 @Aoe{r=5,t=damageable}
      - DO_HARM:2 @Aoe{r=5,t=damageable}
      - MESSAGE:§c§l** DIVINE IMMOLATION ** @Aoe{r=5,t=damageable}
paradox:
  display: '%group-color%Paradox'
  description: |-
    Encantamiento del alma pasiva.
    Cura a todos los aliados cercanos en un enorme
    área a su alrededor para una parte de
    Todo el daño le dio.
  applies-to: ꐚ
  type: DEFENSE
  group: SOUL
  applies:
  - ALL_ARMOR
  levels:
    '1':
      chance: 13
      cooldown: 5
      souls: 5
      effects:
      - PARTICLE:HEART:20:2@Aoe{r=5,t=undamageable}
      - ADD_HEALTH:<math>%damage%/4</math> @Aoe{r=5,t=undamageable}
      - MESSAGE:§c§l** PARADOX ** @Aoe{r=5,t=undamageable}
    '2':
      chance: 15
      cooldown: 5
      souls: 5
      effects:
      - PARTICLE:HEART:20:2@Aoe{r=6,t=undamageable}
      - ADD_HEALTH:<math>%damage%/4</math> @Aoe{r=6,t=undamageable}
      - MESSAGE:§c§l** PARADOX ** @Aoe{r=6,t=undamageable}
    '3':
      chance: 17
      cooldown: 5
      souls: 5
      effects:
      - PARTICLE:HEART:20:2@Aoe{r=6,t=undamageable}
      - ADD_HEALTH:<math>%damage%/3</math> @Aoe{r=6,t=undamageable}
      - MESSAGE:§c§l** PARADOX ** @Aoe{r=6,t=undamageable}
    '4':
      chance: 19
      cooldown: 5
      souls: 5
      effects:
      - PARTICLE:HEART:20:2@Aoe{r=7,t=undamageable}
      - ADD_HEALTH:<math>%damage%/3</math> @Aoe{r=7,t=undamageable}
      - MESSAGE:§c§l** PARADOX ** @Aoe{r=7,t=undamageable}
    '5':
      chance: 12
      cooldown: 5
      souls: 5
      effects:
      - PARTICLE:HEART:20:2@Aoe{r=7,t=undamageable}
      - ADD_HEALTH:<math>%damage%/2</math> @Aoe{r=7,t=undamageable}
      - MESSAGE:§c§l** PARADOX ** @Aoe{r=7,t=undamageable}
soulgrind:
  display: '%group-color%SoulGrind'
  description: Oportunidad aleatoria de obtener una almas para matar monstruos.
  applies-to: ꐚ
  type: KILL_MOB
  group: MASTERY
  applies:
  - ALL_SWORD
  levels:
    '1':
      chance: 4
      cooldown: 80
      effects:
      - CONSOLE_COMMAND:ae giveitem %attacker name% soulgem 1 4
    '2':
      chance: 6
      cooldown: 65
      effects:
      - CONSOLE_COMMAND:ae giveitem %attacker name% soulgem 1 6
    '3':
      chance: 8
      cooldown: 55
      effects:
      - CONSOLE_COMMAND:ae giveitem %attacker name% soulgem 1 10
neutralize:
  display: '%group-color%Neutralize'
  description: |-
    Oportunidad de deshabilitar todos los encantamientos defensivos enemigos durante 7 segundos.
    Este efecto puede acumularse con silence.
  applies-to: ꐚ
  type: ATTACK
  group: MASTERY
  applies:
  - ALL_SWORD
  levels:
    '1':
      chance: 1
      cooldown: 140
      effects:
      - DISABLE_ACTIVATION:cactus:7 @Victim
      - DISABLE_ACTIVATION:enlighted:7 @Victim
      - DISABLE_ACTIVATION:angelic:7 @Victim
      - DISABLE_ACTIVATION:divineenlighted:7 @Victim
      - DISABLE_ACTIVATION:dodge:7 @Victim
      - DISABLE_ACTIVATION:valor:7 @Victim
      - DISABLE_ACTIVATION:mightycactus:7 @Victim
      - MESSAGE:§4§l* Neutralized§r §4[7s] §5§l* @Victim
    '2':
      chance: 2
      cooldown: 120
      effects:
      - DISABLE_ACTIVATION:cactus:7 @Victim
      - DISABLE_ACTIVATION:enlighted:7 @Victim
      - DISABLE_ACTIVATION:angelic:7 @Victim
      - DISABLE_ACTIVATION:divineenlighted:7 @Victim
      - DISABLE_ACTIVATION:dodge:7 @Victim
      - DISABLE_ACTIVATION:valor:7 @Victim
      - DISABLE_ACTIVATION:mightycactus:7 @Victim
      - MESSAGE:§4§l* Neutralized§r §4[7s] §5§l* @Victim
    '3':
      chance: 3
      cooldown: 100
      effects:
      - DISABLE_ACTIVATION:cactus:7 @Victim
      - DISABLE_ACTIVATION:enlighted:7 @Victim
      - DISABLE_ACTIVATION:angelic:7 @Victim
      - DISABLE_ACTIVATION:divineenlighted:7 @Victim
      - DISABLE_ACTIVATION:dodge:7 @Victim
      - DISABLE_ACTIVATION:valor:7 @Victim
      - DISABLE_ACTIVATION:mightycactus:7 @Victim
      - MESSAGE:§4§l* Neutralized§r §4[7s] §5§l* @Victim
    '4':
      chance: 4
      cooldown: 80
      effects:
      - DISABLE_ACTIVATION:cactus:7 @Victim
      - DISABLE_ACTIVATION:enlighted:7 @Victim
      - DISABLE_ACTIVATION:angelic:7 @Victim
      - DISABLE_ACTIVATION:divineenlighted:7 @Victim
      - DISABLE_ACTIVATION:dodge:7 @Victim
      - DISABLE_ACTIVATION:valor:7 @Victim
      - DISABLE_ACTIVATION:mightycactus:7 @Victim
      - MESSAGE:§4§l* Neutralized§r §4[7s] §5§l* @Victim
    '5':
      chance: 6
      cooldown: 20
      effects:
      - DISABLE_ACTIVATION:cactus:5 @Victim
      - DISABLE_ACTIVATION:enlighted:5 @Victim
      - DISABLE_ACTIVATION:angelic:5 @Victim
      - DISABLE_ACTIVATION:divineenlighted:5 %victim
      - DISABLE_ACTIVATION:dodge:5 @Victim
      - DISABLE_ACTIVATION:valor:5 @Victim
      - DISABLE_ACTIVATION:mightycactus:5 @Victim
      - DISABLE_ACTIVATION:lucky:5 @Victim
      - MESSAGE:§4§l* Neutralized§r §4[5s] §4§l* @Victim
halloweenify:
  display: '%group-color%Halloweenify'
  description: Oportunidad de reemplazar el casco de tus oponentes a una calabaza por un corto tiempo.
  applies-to: ꐚ ꐝ
  type: ATTACK
  group: MASTERY
  applies:
  - ALL_SWORD
  - ALL_AXE
  levels:
    '1':
      chance: 1.8
      cooldown: 20
      effects:
      - PUMPKIN:40 @Victim
      - MESSAGE:§e§l** HALLOWEENIFY ** @Victim
      - PLAY_SOUND_OUTLOUD:ANVIL_DROP
    '2':
      chance: 3.6
      cooldown: 20
      effects:
      - PUMPKIN:40 @Victim
      - MESSAGE:§e§l** HALLOWEENIFY ** @Victim
      - PLAY_SOUND_OUTLOUD:ANVIL_DROP
    '3':
      chance: 4.4
      cooldown: 20
      effects:
      - PUMPKIN:60 @Victim
      - MESSAGE:§e§l** HALLOWEENIFY ** @Victim
      - PLAY_SOUND_OUTLOUD:ANVIL_DROP
    '4':
      chance: 5.2
      cooldown: 20
      effects:
      - PUMPKIN:60 @Victim
      - MESSAGE:§e§l** HALLOWEENIFY ** @Victim
      - PLAY_SOUND_OUTLOUD:ANVIL_DROP
    '5':
      chance: 6
      cooldown: 20
      effects:
      - PUMPKIN:80 @Victim
      - MESSAGE:§e§l** HALLOWEENIFY ** @Victim
      - PLAY_SOUND_OUTLOUD:ANVIL_DROP
markofthebeast:
  display: '%group-color%Mark of the Beast'
  description: |-
    Una vez que un enemigo está afectado por la marca
    Todo el daño entrante aumenta en 2x para
    hasta 5 segundos
  applies-to: ꐤ ꐞ ꐧ ꐥ
  type: DEFENSE
  group: MASTERY
  applies:
  - ALL_ARMOR
  levels:
    '1':
      chance: 4
      cooldown: 600
      effects:
      - MESSAGE:§c§l* MARK OF THE BEAST [§72s§c§l] * @Victim
      - INCREASE_DAMAGE:50 @Attacker
      - WAIT:20
      - INCREASE_DAMAGE:50 @Attacker
      - WAIT:20
    '2':
      chance: 6
      cooldown: 500
      effects:
      - MESSAGE:§c§l* MARK OF THE BEAST [§72s§c§l] * @Victim
      - INCREASE_DAMAGE:50 @Attacker
      - WAIT:20
      - INCREASE_DAMAGE:50 @Attacker
      - WAIT:20
    '3':
      chance: 8
      cooldown: 400
      effects:
      - MESSAGE:§c§l* MARK OF THE BEAST [§72s§c§l] * @Victim
      - INCREASE_DAMAGE:50 @Attacker
      - WAIT:20
      - INCREASE_DAMAGE:50 @Attacker
      - WAIT:20
      - INCREASE_DAMAGE:50 @Attacker
      - WAIT:20
    '4':
      chance: 10
      cooldown: 300
      effects:
      - MESSAGE:§c§l* MARK OF THE BEAST [§73s§c§l] * @Victim
      - INCREASE_DAMAGE:50 @Attacker
      - WAIT:20
      - INCREASE_DAMAGE:50 @Attacker
      - WAIT:20
      - INCREASE_DAMAGE:50 @Attacker
      - WAIT:20
    '5':
      chance: 13
      cooldown: 200
      effects:
      - MESSAGE:§c§l* MARK OF THE BEAST [§74s§c§l] * @Victim
      - INCREASE_DAMAGE:50 @Attacker
      - WAIT:20
      - INCREASE_DAMAGE:50 @Attacker
      - WAIT:20
      - INCREASE_DAMAGE:50 @Attacker
      - WAIT:20
      - INCREASE_DAMAGE:50 @Attacker
      - WAIT:20
    '6':
      chance: 16
      cooldown: 100
      effects:
      - MESSAGE:§c§l* MARK OF THE BEAST [§74s§c§l] * @Victim
      - INCREASE_DAMAGE:50 @Attacker
      - WAIT:20
      - INCREASE_DAMAGE:50 @Attacker
      - WAIT:20
      - INCREASE_DAMAGE:50 @Attacker
      - WAIT:20
      - INCREASE_DAMAGE:50 @Attacker
      - WAIT:20
horrify:
  display: '%group-color%Horrify'
  description: Oportunidad de infligir enemigos dentro de un radio de 32x32 con &6Horror&r.
  applies-to: ꐤ ꐞ ꐧ ꐥ
  type: DEFENSE
  group: MASTERY
  applies:
  - ALL_ARMOR
  levels:
    '1':
      chance: 1.5
      cooldown: 120
      effects:
      - POTION:CONFUSION:23:40 @Aoe{r=32,t=damageable}
      - POTION:SLOW:23:40 @Aoe{r=32,t=damageable}
      - POTION:SLOW_DIGGING:23:40 @Aoe{r=32,t=damageable}
      - MESSAGE:§4§l** HORRIFY ** <aeo> radius=32 target=damageable </aoe>
    '2':
      chance: 3.1
      cooldown: 120
      effects:
      - POTION:CONFUSION:23:40 @Aoe{r=32,t=damageable}
      - POTION:SLOW:23:40 @Aoe{r=32,t=damageable}
      - POTION:SLOW_DIGGING:23:40 @Aoe{r=32,t=damageable}
      - MESSAGE:§4§l** HORRIFY ** <aeo> radius=32 target=damageable </aoe>
    '3':
      chance: 4.1
      cooldown: 120
      effects:
      - POTION:CONFUSION:23:60 @Aoe{r=32,t=damageable}
      - POTION:SLOW:23:60 @Aoe{r=32,t=damageable}
      - POTION:SLOW_DIGGING:23:60 @Aoe{r=32,t=damageable}
      - MESSAGE:§4§l** HORRIFY ** <aeo> radius=32 target=damageable </aoe>
    '4':
      chance: 5.3
      cooldown: 120
      effects:
      - POTION:CONFUSION:23:80 @Aoe{r=32,t=damageable}
      - POTION:SLOW:23:80 @Aoe{r=32,t=damageable}
      - POTION:SLOW_DIGGING:23:80 @Aoe{r=32,t=damageable}
      - MESSAGE:§4§l** HORRIFY ** <aeo> radius=32 target=damageable </aoe>
chainlifesteal:
  display: '%group-color%Chain Lifesteal'
  description: |-
    Una oportunidad para recuperar la salud de múltiples
    enemigos cerca de tu objetivo dañado basado en el nivel
  applies-to: ꐧ
  type: ATTACK
  group: MASTERY
  applies:
  - ALL_CHESTPLATE
  levels:
    '1':
      chance: 1.8
      cooldown: 120
      effects:
      - STEAL_HEALTH:<random number>1-3</random number> @Aoe{r=6,t=damageable}
      - MESSAGE:§4§l** CHAIN LIFESTEAL ** §7(-5 §cHP§7) @Aoe{r=6,t=damageable}
    '2':
      chance: 3.9
      cooldown: 120
      effects:
      - STEAL_HEALTH:<random number>1-3</random number> @Aoe{r=6,t=damageable}
      - MESSAGE:§4§l** CHAIN LIFESTEAL ** §7(-5 §cHP§7) @Aoe{r=6,t=damageable}
soulsiphone:
  display: '%group-color%Soul Siphone'
  description: |-
    Procediendo en eventos de daño saliente de esta encantadora Syphons Souls
    ¡y la durabilidad de los enemigos en grandes cantidades!.
  applies-to: ꐥ
  type: DEFENSE
  group: MASTERY
  applies:
  - ALL_BOOTS
  levels:
    '1':
      chance: 6.1
      cooldown: 60
      effects:
      - DAMAGE_ARMOR:10 @Attacker
      - REMOVE_SOULS:200 @Attacker
      - MESSAGE:§4§l** SOUL SIPHONE ** §7(%victim name%)
    '2':
      chance: 8.1
      cooldown: 60
      effects:
      - DAMAGE_ARMOR:15 @Attacker
      - REMOVE_SOULS:200 @Attacker
      - MESSAGE:§4§l** SOUL SIPHONE ** §7(%victim name%)
    '3':
      chance: 10.4
      cooldown: 60
      effects:
      - DAMAGE_ARMOR:20 @Attacker
      - REMOVE_SOULS:200 @Attacker
      - MESSAGE:§4§l** SOUL SIPHONE ** §7(%victim name%)
    '4':
      chance: 13.5
      cooldown: 60
      effects:
      - DAMAGE_ARMOR:30 @Attacker
      - REMOVE_SOULS:200 @Attacker
      - MESSAGE:§4§l** SOUL SIPHONE ** §7(%victim name%)
