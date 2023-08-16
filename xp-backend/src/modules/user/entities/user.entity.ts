import { DateTime } from 'luxon';
import { ExperimentView } from 'src/modules/experiment/entities/experiment-view.entity';
import { Experiment } from 'src/modules/experiment/entities/experiment.entity';
import { Observation } from 'src/modules/observation/entities/observation.entity';
import { Subscription } from 'src/modules/profile/entities/Subscription';
import {
  Column,
  CreateDateColumn,
  DeleteDateColumn,
  Entity,
  Index,
  OneToMany,
  PrimaryGeneratedColumn,
} from 'typeorm';

@Entity()
export class User {
  @PrimaryGeneratedColumn()
  id: number;

  @Column('bigint', { nullable: true, unique: true })
  tg_id: number;

  @Column('varchar', { length: 32, nullable: true, unique: true })
  username: string;

  @Column('char', { length: 60, nullable: false, select: false })
  password_hash: string;

  @Index()
  @CreateDateColumn({
    select: false,
    type: 'timestamptz',
    transformer: {
      from: (date?: Date) => DateTime?.fromJSDate(date),
      to: (dateTime?: DateTime) => dateTime?.toJSDate(),
    },
  })
  created_at: DateTime;

  @Index()
  @DeleteDateColumn({
    select: false,
    type: 'timestamptz',
    transformer: {
      from: (date: Date) => DateTime?.fromJSDate(date),
      to: (dateTime: DateTime) => dateTime?.toJSDate(),
    },
  })
  deleted_at: DateTime;

  @OneToMany(() => Observation, (entity) => entity.user)
  observations: Observation[];

  @OneToMany(() => Experiment, (entity) => entity.user)
  experiments: Observation[];

  @OneToMany(() => Subscription, (entity) => entity.followee)
  followers: Subscription[];

  @OneToMany(() => Subscription, (entity) => entity.follower)
  followee: Subscription[];

  @OneToMany(() => ExperimentView, (entity) => entity.user)
  seen_experiments: ExperimentView[];
}
