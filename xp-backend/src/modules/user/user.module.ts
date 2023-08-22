import { Module } from '@nestjs/common';
import { TypeOrmModule } from '@nestjs/typeorm';
import { User } from './entities/user.entity';
import { UserRepository } from './repositories/user.repository';
import { Subscription } from './entities/Subscription.entity';
import { SubscriptionRepository } from './repositories/subscription.repository';

@Module({
  imports: [TypeOrmModule.forFeature([User, Subscription])],
  providers: [UserRepository, SubscriptionRepository],
  exports: [UserRepository, SubscriptionRepository],
})
export class UserModule {}
