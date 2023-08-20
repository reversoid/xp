import { DateTime } from 'luxon';
import { User } from 'src/modules/user/entities/user.entity';
import {
  CreateDateColumn,
  DeleteDateColumn,
  Entity,
  Index,
  ManyToOne,
  PrimaryGeneratedColumn,
} from 'typeorm';
import { Observation } from './observation.entity';

@Entity()
export class ObservationView {
  @PrimaryGeneratedColumn()
  id: number;

  @ManyToOne(() => User, (user) => user.observations, {
    nullable: false,
    onDelete: 'CASCADE',
  })
  user: User;

  @ManyToOne(() => Observation, (entity) => entity.views, {
    nullable: false,
    onDelete: 'CASCADE',
  })
  observation: Observation;

  @CreateDateColumn({
    select: false,
    type: 'timestamptz',
    transformer: {
      from: (date: Date) => DateTime?.fromJSDate(date),
      to: (dateTime: DateTime) => dateTime?.toJSDate(),
    },
  })
  seen_at: DateTime;

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
}
