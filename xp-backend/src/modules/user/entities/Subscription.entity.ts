import { ApiProperty } from '@nestjs/swagger';
import { DateTime } from 'luxon';
import { User } from 'src/modules/user/entities/user.entity';
import {
  CreateDateColumn,
  DeleteDateColumn,
  Entity,
  JoinColumn,
  ManyToOne,
  PrimaryGeneratedColumn,
} from 'typeorm';

@Entity()
export class Subscription {
  @PrimaryGeneratedColumn()
  id: number;

  @ManyToOne(() => User, (user) => user.followedSubscriptions, {
    nullable: false,
  })
  @JoinColumn({ name: 'follower_id' })
  follower: User;

  @ManyToOne(() => User, (user) => user.followerSubscriptions, {
    nullable: false,
  })
  @JoinColumn({ name: 'followed_id' })
  followed: User;

  @ApiProperty({
    type: 'string',
    format: 'date-time',
    required: false,
  })
  @DeleteDateColumn({
    select: false,
    type: 'timestamptz',
    transformer: {
      from: (date: Date) => DateTime?.fromJSDate(date),
      to: (dateTime: DateTime) => dateTime?.toJSDate(),
    },
  })
  deleted_at: DateTime;

  @ApiProperty({
    type: 'string',
    format: 'date-time',
    required: false,
  })
  @CreateDateColumn({
    type: 'timestamptz',
    transformer: {
      from: (date: Date) => DateTime?.fromJSDate(date),
      to: (dateTime: DateTime) => dateTime?.toJSDate(),
    },
  })
  created_at: DateTime;
}
