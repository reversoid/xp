import { DateTime } from 'luxon';
import { Observation } from 'src/modules/observation/entities/observation.entity';
import { User } from 'src/modules/user/entities/user.entity';
import { Geo } from 'src/shared/types/Geo.type';
import { MediaGroupItem } from 'src/shared/types/Media-group-item.type';
import {
  Column,
  CreateDateColumn,
  DeleteDateColumn,
  Entity,
  Index,
  JoinTable,
  ManyToMany,
  ManyToOne,
  OneToMany,
  PrimaryGeneratedColumn,
} from 'typeorm';
import { ExperimentView } from './experiment-view.entity';
import { ApiProperty } from '@nestjs/swagger';

export enum ExperimentStatus {
  STARTED = 'STARTED',
  COMPLETED = 'COMPLETED',
  CANCELED = 'CANCELED',
}

@Entity()
export class Experiment {
  @PrimaryGeneratedColumn()
  id: number;

  @ManyToOne(() => User, (user) => user.observations, {
    nullable: false,
    onDelete: 'CASCADE',
  })
  user: User;

  @OneToMany(() => ExperimentView, (view) => view.experiment, {
    nullable: false,
    onDelete: 'CASCADE',
  })
  views: ExperimentView[];

  @Column('text', { nullable: true })
  text?: string;

  @Column('varchar', { nullable: true, length: 256 })
  tg_photo_id?: string;

  @Column('varchar', { nullable: true, length: 256 })
  tg_video_id?: string;

  @Column('varchar', { nullable: true, length: 256 })
  tg_video_note_id?: string;

  @Column('varchar', { nullable: true, length: 256 })
  tg_voice_id?: string;

  @Column('varchar', { nullable: true, length: 256 })
  tg_document_id?: string;

  @Column('jsonb', { nullable: true, array: false })
  tg_media_group?: MediaGroupItem[];

  @Column('jsonb', { nullable: true })
  geo?: Geo;

  @Index()
  @Column('enum', {
    enum: ExperimentStatus,
    default: ExperimentStatus.STARTED,
    nullable: false,
  })
  status: ExperimentStatus;

  @ApiProperty({
    type: 'string',
    format: 'date-time',
    required: false,
  })
  @Index()
  @Column('timestamptz', {
    nullable: true,
    transformer: {
      from: (date: Date) => DateTime?.fromJSDate(date),
      to: (dateTime: DateTime) => dateTime?.toJSDate(),
    },
  })
  completed_at: DateTime;

  @ApiProperty({
    type: 'string',
    format: 'date-time',
    required: false,
  })
  @Index()
  @Column('timestamptz', {
    nullable: false,
    transformer: {
      from: (date: Date) => DateTime?.fromJSDate(date),
      to: (dateTime: DateTime) => dateTime?.toJSDate(),
    },
  })
  complete_by: DateTime;

  @Column('varchar', { nullable: true, length: 256, array: true })
  file_urls?: string[];

  @ManyToMany(() => Observation)
  @JoinTable()
  observations: Observation[];

  @ApiProperty({
    type: 'string',
    format: 'date-time',
    required: false,
  })
  @Index()
  @CreateDateColumn({
    select: false,
    type: 'timestamptz',
    transformer: {
      from: (date: Date) => DateTime?.fromJSDate(date),
      to: (dateTime: DateTime) => dateTime?.toJSDate(),
    },
  })
  created_at: DateTime;

  @ApiProperty({
    type: 'string',
    format: 'date-time',
    required: false,
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
