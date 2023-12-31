import { DateTime } from 'luxon';
import { User } from 'src/modules/user/entities/user.entity';
import { MediaGroupItem } from 'src/shared/types/Media-group-item.type';
import {
  Column,
  CreateDateColumn,
  DeleteDateColumn,
  Entity,
  Index,
  ManyToOne,
  OneToMany,
  PrimaryGeneratedColumn,
} from 'typeorm';
import { ObservationView } from './observation-view.entity';
import { ApiProperty } from '@nestjs/swagger';

@Entity()
export class Observation {
  @PrimaryGeneratedColumn()
  id: number;

  @ManyToOne(() => User, (user) => user.observations, {
    nullable: false,
    onDelete: 'CASCADE',
  })
  user: User;

  @Column('text', { nullable: true })
  text?: string;

  @Column('varchar', { nullable: true, length: 256 })
  tg_photo_id?: string;

  @Column('varchar', { nullable: true, length: 256 })
  tg_document_id?: string;

  @Column('varchar', { nullable: true, length: 256 })
  tg_voice_id?: string;

  @Column('varchar', { nullable: true, length: 256 })
  tg_video_id?: string;

  @Column('varchar', { nullable: true, length: 256 })
  tg_video_note_id?: string;

  @Column('varchar', { nullable: true, length: 256, array: true })
  file_urls?: string[];

  @Column('jsonb', { nullable: true, array: true })
  tg_media_group?: MediaGroupItem[];

  @ApiProperty({
    type: 'string',
    format: 'date-time',
    required: false,
  })
  @Index()
  @CreateDateColumn({
    select: true,
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

  @OneToMany(() => ObservationView, (view) => view.observation, {
    nullable: false,
    onDelete: 'CASCADE',
  })
  views: ObservationView[];
}
