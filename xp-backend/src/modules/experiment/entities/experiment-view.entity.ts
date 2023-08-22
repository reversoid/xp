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
import { Experiment } from './experiment.entity';
import { ApiProperty } from '@nestjs/swagger';

@Entity()
export class ExperimentView {
  @PrimaryGeneratedColumn()
  id: number;

  @ManyToOne(() => User, (user) => user.observations, {
    nullable: false,
    onDelete: 'CASCADE',
  })
  user: User;

  @ManyToOne(() => Experiment, (entity) => entity.views, {
    nullable: false,
    onDelete: 'CASCADE',
  })
  experiment: Experiment;

  @ApiProperty({
    type: 'string',
    format: 'date-time',
    required: false,
    description: 'Seen at date',
  })
  @CreateDateColumn({
    select: false,
    type: 'timestamptz',
    transformer: {
      from: (date: Date) => DateTime?.fromJSDate(date),
      to: (dateTime: DateTime) => dateTime?.toJSDate(),
    },
  })
  seen_at: DateTime;

  @ApiProperty({
    type: 'string',
    format: 'date-time',
    required: false,
    description: 'deleted at date',
    nullable: true,
  })
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
