import { Module } from '@nestjs/common';
import { FeedController } from './feed.controller';
import { FeedService } from './feed.service';
import { ExperimentModule } from '../experiment/experiment.module';
import { UserModule } from '../user/user.module';

@Module({
  imports: [ExperimentModule, UserModule],
  controllers: [FeedController],
  providers: [FeedService],
})
export class FeedModule {}
